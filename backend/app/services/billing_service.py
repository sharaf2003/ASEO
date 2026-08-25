import uuid


from sqlalchemy.orm import Session


from app.models.invoice import Invoice


from app.repositories.invoice_repository import (
    InvoiceRepository
)

from app.repositories.usage_billing_repository import (
    UsageBillingRepository
)



class BillingService:

    """
    ASEO SaaS Billing Service.

    Responsibilities:

    - Create invoices
    - Calculate plan prices
    - Manage billing records
    """





    PLAN_PRICES = {


        "free": 0,


        "pro": 99,


        "enterprise": 499

    }





    def __init__(self):

        self.repository = InvoiceRepository()

        self.usage_billing_repository = UsageBillingRepository()



    # =====================================
    # Create Invoice
    # =====================================


    def create_invoice(

        self,

        db: Session,

        organization_id: int,

        plan: str

    ):


        amount = self.PLAN_PRICES.get(

            plan,

            0

        )



        invoice = Invoice(


            organization_id=organization_id,


            invoice_number=(

                "INV-"

                + str(uuid.uuid4())[:8].upper()

            ),


            plan=plan,


            amount=amount,


            currency="USD",


            status="pending"

        )



        return self.repository.create(

            db,

            invoice

        )





    # =====================================
    # Get Organization Invoices
    # =====================================


    def get_invoices(

        self,

        db: Session,

        organization_id: int

    ):


        return self.repository.get_by_organization(

            db,

            organization_id

        )





    # =====================================
    # Mark Invoice Paid
    # =====================================


    def mark_paid(

        self,

        db: Session,

        invoice: Invoice

    ):


        return self.repository.update(

            db,

            invoice,

            {

                "status": "paid"

            }

        )
    

    # =====================================
    # Create Usage Invoice
    # =====================================


    def create_usage_invoice(

        self,

        db: Session,

        organization_id: int,

        month: str

    ):


        usage_billing = self.usage_billing_repository.get_by_month(

            db,

            organization_id,

            month

        )


        if not usage_billing:

            return None





        invoice = Invoice(

            organization_id=organization_id,

            invoice_number=(

                "USAGE-"

                + month.replace("-", "")

            ),

            plan="usage",

            amount=usage_billing.cost,

            currency="USD",

            status="pending"

        )



        return self.repository.create(

            db,

            invoice

        )