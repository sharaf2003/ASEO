from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session


from app.services.subscription_service import (
    SubscriptionService
)


from app.repositories.subscription_repository import (
    SubscriptionRepository
)





class SubscriptionLifecycleService:

    """
    ASEO Subscription Lifecycle Service.

    Responsibilities:

    - Check subscription status
    - Expire subscriptions
    - Renew subscriptions
    - Handle lifecycle changes
    """





    def __init__(self):

        self.repository = SubscriptionRepository()

        self.subscription_service = SubscriptionService()





    # =====================================
    # Check Subscription Status
    # =====================================


    def check_status(

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





        if subscription.expires_at:


            if subscription.expires_at < datetime.now(timezone.utc):


                self.repository.update(

                    db,

                    subscription,

                    {

                        "status": "expired"

                    }

                )



        return subscription





    # =====================================
    # Renew Subscription
    # =====================================


    def renew_subscription(

        self,

        db: Session,

        organization_id: int,

        months: int = 1

    ):


        subscription = self.repository.get_by_organization(

            db,

            organization_id

        )



        if not subscription:

            subscription = self.subscription_service.create_default_subscription(

                db,

                organization_id

            )





        new_expiry = datetime.now(timezone.utc) + timedelta(
            days=30 * months
        )




        return self.repository.update(

            db,

            subscription,

            {

                "status": "active",

                "expires_at": new_expiry

            }

        )