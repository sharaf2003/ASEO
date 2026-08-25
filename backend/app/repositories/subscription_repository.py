from sqlalchemy.orm import Session

from app.models.subscription import Subscription





class SubscriptionRepository:

    """
    ASEO Subscription Repository.
    """



    # =====================================
    # Create Subscription
    # =====================================


    def create(

        self,

        db: Session,

        subscription: Subscription

    ):


        db.add(subscription)

        db.commit()

        db.refresh(subscription)


        return subscription





    # =====================================
    # Get Organization Subscription
    # =====================================


    def get_by_organization(

        self,

        db: Session,

        organization_id: int

    ):


        return (

            db.query(Subscription)

            .filter(

                Subscription.organization_id == organization_id

            )

            .first()

        )





    # =====================================
    # Update Subscription
    # =====================================


    def update(

        self,

        db: Session,

        subscription: Subscription,

        data: dict

    ):


        for key, value in data.items():

            setattr(

                subscription,

                key,

                value

            )


        db.commit()

        db.refresh(subscription)


        return subscription





    # =====================================
    # Cancel Subscription
    # =====================================


    def cancel(

        self,

        db: Session,

        subscription: Subscription

    ):


        subscription.status = "cancelled"


        db.commit()

        db.refresh(subscription)


        return subscription