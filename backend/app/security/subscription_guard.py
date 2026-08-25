from datetime import datetime, timezone


from fastapi import HTTPException

from sqlalchemy.orm import Session


from app.repositories.subscription_repository import (
    SubscriptionRepository
)





class SubscriptionGuard:

    """
    ASEO Subscription Access Guard.

    Controls API access based on subscription state.
    """





    def __init__(self):

        self.repository = SubscriptionRepository()





    # =====================================
    # Check Subscription Access
    # =====================================


    def check_access(

        self,

        db: Session,

        organization_id: int

    ):


        subscription = self.repository.get_by_organization(

            db,

            organization_id

        )



        if not subscription:

            raise HTTPException(

                status_code=403,

                detail="No active subscription"

            )





        if subscription.expires_at:


            if subscription.expires_at < datetime.now(timezone.utc):


                raise HTTPException(

                    status_code=403,

                    detail="Subscription expired"

                )





        allowed_statuses = [

            "active",

            "grace_period"

        ]





        if subscription.status not in allowed_statuses:


            raise HTTPException(

                status_code=403,

                detail=f"Subscription {subscription.status}"

            )



        return True