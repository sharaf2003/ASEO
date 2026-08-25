from datetime import datetime, timedelta, timezone


from sqlalchemy.orm import Session


from app.repositories.subscription_repository import (
    SubscriptionRepository
)





class SubscriptionGraceService:

    """
    ASEO Subscription Grace Period Service.

    Responsibilities:

    - Handle failed payments
    - Start grace period
    - Suspend subscriptions
    """





    GRACE_PERIOD_DAYS = 7





    def __init__(self):

        self.repository = SubscriptionRepository()





    # =====================================
    # Start Grace Period
    # =====================================


    def start_grace_period(

        self,

        db: Session,

        organization_id: int

    ):


        subscription = self.repository.get_by_organization(

            db,

            organization_id

        )



        if not subscription:

            return None





        grace_end = datetime.now(timezone.utc) + timedelta(

            days=self.GRACE_PERIOD_DAYS

        )





        return self.repository.update(

            db,

            subscription,

            {

                "status": "grace_period",

                "expires_at": grace_end

            }

        )





    # =====================================
    # Suspend Subscription
    # =====================================


    def suspend_subscription(

        self,

        db: Session,

        organization_id: int

    ):


        subscription = self.repository.get_by_organization(

            db,

            organization_id

        )



        if not subscription:

            return None





        return self.repository.update(

            db,

            subscription,

            {

                "status": "suspended"

            }

        )