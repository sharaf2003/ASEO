from sqlalchemy.orm import Session


from app.models.payment import Payment





class PaymentRepository:

    """
    ASEO Payment Repository.
    """



    # =====================================
    # Create Payment
    # =====================================


    def create(

        self,

        db: Session,

        payment: Payment

    ):


        db.add(payment)

        db.commit()

        db.refresh(payment)


        return payment





    # =====================================
    # Get Payment By ID
    # =====================================


    def get_by_id(

        self,

        db: Session,

        payment_id: int

    ):


        return (

            db.query(Payment)

            .filter(

                Payment.id == payment_id

            )

            .first()

        )





    # =====================================
    # Get Organization Payments
    # =====================================


    def get_by_organization(

        self,

        db: Session,

        organization_id: int

    ):


        return (

            db.query(Payment)

            .filter(

                Payment.organization_id == organization_id

            )

            .order_by(

                Payment.created_at.desc()

            )

            .all()

        )





    # =====================================
    # Update Payment
    # =====================================


    def update(

        self,

        db: Session,

        payment: Payment,

        data: dict

    ):


        for key, value in data.items():

            setattr(

                payment,

                key,

                value

            )


        db.commit()

        db.refresh(payment)


        return payment


    # =====================================
    # Get By Transaction ID
    # =====================================


    def get_by_transaction_id(

        self,

        db: Session,

        transaction_id: str

    ):


        return (

            db.query(Payment)

            .filter(

                Payment.transaction_id == transaction_id

            )

            .first()

        )