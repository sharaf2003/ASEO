from sqlalchemy.orm import Session


from app.models.subscription import Subscription


from app.repositories.subscription_repository import (
    SubscriptionRepository
)


from app.repositories.api_key_repository import (
    APIKeyRepository
)


from app.repositories.api_rate_limit_repository import (
    APIRateLimitRepository
)


from app.services.billing_service import (
    BillingService
)





class SubscriptionService:

    """
    ASEO Subscription Service.
    """



    PLANS = {


        "free": {

            "requests_per_minute": 100,

            "requests_per_day": 10000,

            "requests_per_month": 100000

        },


        "pro": {

            "requests_per_minute": 1000,

            "requests_per_day": 100000,

            "requests_per_month": 1000000

        },


        "enterprise": {

            "requests_per_minute": 10000,

            "requests_per_day": 1000000,

            "requests_per_month": 10000000

        }

    }





    def __init__(self):

        self.repository = SubscriptionRepository()

        self.api_key_repository = APIKeyRepository()

        self.api_rate_limit_repository = APIRateLimitRepository()

        self.billing_service = BillingService()





    # =====================================
    # Create Default Subscription
    # =====================================


    def create_default_subscription(

        self,

        db: Session,

        organization_id: int

    ):


        subscription = Subscription(

            organization_id=organization_id,

            plan="free",

            status="active"

        )


        return self.repository.create(

            db,

            subscription

        )





    # =====================================
    # Get Subscription
    # =====================================


    def get_subscription(

        self,

        db: Session,

        organization_id: int

    ):


        return self.repository.get_by_organization(

            db,

            organization_id

        )





    # =====================================
    # Update API Rate Limits
    # =====================================


    def update_api_limits(

        self,

        db: Session,

        organization_id: int,

        plan: str

    ):


        limits = self.get_plan_limits(

            plan

        )



        api_keys = self.api_key_repository.get_by_organization(

            db,

            organization_id

        )



        updated = 0



        for api_key in api_keys:


            rate_limit = self.api_rate_limit_repository.get_by_api_key(

                db,

                api_key.id

            )



            if rate_limit:


                self.api_rate_limit_repository.update(

                    db,

                    rate_limit,

                    {


                        "requests_per_minute":

                            limits["requests_per_minute"],


                        "requests_per_day":

                            limits["requests_per_day"],


                        "requests_per_month":

                            limits["requests_per_month"]

                    }

                )


                updated += 1



        return updated





    # =====================================
    # Change Plan
    # =====================================


    def change_plan(

        self,

        db: Session,

        organization_id: int,

        plan: str

    ):


        subscription = self.get_subscription(

            db,

            organization_id

        )



        if not subscription:


            subscription = self.create_default_subscription(

                db,

                organization_id

            )





        updated_subscription = self.repository.update(

            db,

            subscription,

            {

                "plan": plan,

                "status": "active"

            }

        )





        updated_keys = self.update_api_limits(

            db,

            organization_id,

            plan

        )





        invoice = self.billing_service.create_invoice(

            db,

            organization_id,

            plan

        )





        return {


            "subscription":

                updated_subscription,


            "updated_api_keys":

                updated_keys,


            "invoice":

                invoice

        }





    # =====================================
    # Get Plan Limits
    # =====================================


    def get_plan_limits(

        self,

        plan: str

    ):


        return self.PLANS.get(

            plan,

            self.PLANS["free"]

        )