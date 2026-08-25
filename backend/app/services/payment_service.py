import uuid


from sqlalchemy.orm import Session


from app.models.payment import Payment


from app.repositories.payment_repository import (
    PaymentRepository
)


from app.repositories.invoice_repository import (
    InvoiceRepository
)


from app.services.subscription_service import (
    SubscriptionService
)


from app.services.subscription_lifecycle_service import (
    SubscriptionLifecycleService
)


from app.services.subscription_grace_service import (
    SubscriptionGraceService
)


from app.services.audit_service import (
    AuditService
)





class PaymentService:

    """
    ASEO Payment Service.

    Responsibilities:

    - Process payments
    - Update invoices
    - Activate subscriptions
    - Audit payment events
    """





    def __init__(self):

        self.repository = PaymentRepository()

        self.invoice_repository = InvoiceRepository()

        self.subscription_service = SubscriptionService()

        self.subscription_lifecycle_service = SubscriptionLifecycleService()

        self.subscription_grace_service = SubscriptionGraceService()

        self.audit_service = AuditService()





    # =====================================
    # Create Payment
    # =====================================


    def create_payment(

        self,

        db: Session,

        organization_id: int,

        invoice_id: int,

        amount: float,

        provider: str = "manual"

    ):


        transaction_id = (

            "PAY-"

            + str(uuid.uuid4())[:8].upper()

        )



        payment = Payment(

            organization_id=organization_id,

            invoice_id=invoice_id,

            transaction_id=transaction_id,

            amount=amount,

            currency="USD",

            provider=provider,

            status="completed"

        )



        created_payment = self.repository.create(

            db,

            payment

        )



        invoice = self.invoice_repository.get_by_id(

            db,

            invoice_id

        )



        if invoice:


            self.invoice_repository.update(

                db,

                invoice,

                {

                    "status": "paid"

                }

            )


            self.subscription_lifecycle_service.renew_subscription(

                db,

                organization_id,

                1

            )


            self.audit_service.log_event(

                db,

                action="PAYMENT_COMPLETED",

                description="Payment completed successfully",

                organization_id=organization_id

            )



        return created_payment





    # =====================================
    # Get Organization Payments
    # =====================================


    def get_payments(

        self,

        db: Session,

        organization_id: int

    ):


        return self.repository.get_by_organization(

            db,

            organization_id

        )





    # =====================================
    # Handle Payment Webhook
    # =====================================


    def handle_webhook(

        self,

        db: Session,

        transaction_id: str,

        invoice_id: int,

        status: str,

        provider: str

    ):


        payment = self.repository.get_by_transaction_id(

            db,

            transaction_id

        )


        if not payment:


            payment = Payment(

                organization_id=0,

                invoice_id=invoice_id,

                transaction_id=transaction_id,

                amount=0,

                currency="USD",

                provider=provider,

                status=status

            )


            payment = self.repository.create(

                db,

                payment

            )


        else:


            payment = self.repository.update(

                db,

                payment,

                {

                    "status": status

                }

            )



        invoice = self.invoice_repository.get_by_id(

            db,

            invoice_id

        )



        if invoice and status == "completed":


            self.invoice_repository.update(

                db,

                invoice,

                {

                    "status": "paid"

                }

            )


            self.subscription_lifecycle_service.renew_subscription(

                db,

                payment.organization_id,

                1

            )


            self.audit_service.log_event(

                db,

                action="PAYMENT_COMPLETED",

                description="Payment webhook completed",

                organization_id=payment.organization_id

            )



        if invoice and status == "failed":


            self.subscription_grace_service.start_grace_period(

                db,

                payment.organization_id

            )


            self.audit_service.log_event(

                db,

                action="PAYMENT_FAILED",

                description="Payment failed, grace period started",

                organization_id=payment.organization_id

            )


        return payment