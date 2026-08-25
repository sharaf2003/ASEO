from sqlalchemy.orm import Session

from app.models.usage_billing import UsageBilling





class UsageBillingRepository:

    """
    ASEO Usage Billing Repository.
    """



    # =====================================
    # Create Usage Billing
    # =====================================


    def create(

        self,

        db: Session,

        usage_billing: UsageBilling

    ):


        db.add(

            usage_billing

        )

        db.commit()

        db.refresh(

            usage_billing

        )


        return usage_billing





    # =====================================
    # Get By Organization And Month
    # =====================================


    def get_by_month(

        self,

        db: Session,

        organization_id: int,

        month: str

    ):


        return (

            db.query(UsageBilling)

            .filter(

                UsageBilling.organization_id == organization_id,

                UsageBilling.month == month

            )

            .first()

        )





    # =====================================
    # Update Usage Billing
    # =====================================


    def update(

        self,

        db: Session,

        usage_billing: UsageBilling,

        data: dict

    ):


        for key, value in data.items():

            setattr(

                usage_billing,

                key,

                value

            )


        db.commit()

        db.refresh(

            usage_billing

        )


        return usage_billing





    # =====================================
    # Get Organization History
    # =====================================


    def get_history(

        self,

        db: Session,

        organization_id: int

    ):


        return (

            db.query(UsageBilling)

            .filter(

                UsageBilling.organization_id == organization_id

            )

            .order_by(

                UsageBilling.created_at.desc()

            )

            .all()

        )