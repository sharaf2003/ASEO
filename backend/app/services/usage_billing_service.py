from sqlalchemy.orm import Session


from app.models.usage_billing import UsageBilling


from app.repositories.usage_billing_repository import (
    UsageBillingRepository
)


from app.services.subscription_service import (
    SubscriptionService
)


from app.repositories.api_usage_repository import (
    APIUsageRepository
)





class UsageBillingService:

    """
    ASEO Usage Based Billing Service.

    Responsibilities:

    - Calculate monthly API usage
    - Apply plan limits
    - Calculate extra usage cost
    - Store billing usage records
    """





    # Cost per extra request block

    EXTRA_REQUEST_PRICE = 0.0001





    def __init__(self):

        self.repository = UsageBillingRepository()

        self.subscription_service = SubscriptionService()

        self.api_usage_repository = APIUsageRepository()





    # =====================================
    # Calculate Monthly Usage
    # =====================================


    def calculate_monthly_usage(

        self,

        db: Session,

        organization_id: int,

        month: str

    ):


        subscription = self.subscription_service.get_subscription(

            db,

            organization_id

        )



        if not subscription:

            subscription = self.subscription_service.create_default_subscription(

                db,

                organization_id

            )





        limits = self.subscription_service.get_plan_limits(

            subscription.plan

        )





        api_usage = (

            self.api_usage_repository.get_by_organization_month(

                db,

                organization_id,

                month

            )

        )





        total_requests = sum(

            item.requests_count

            for item in api_usage

        )





        included_requests = limits["requests_per_month"]





        extra_requests = max(

            total_requests - included_requests,

            0

        )





        cost = (

            extra_requests

            *

            self.EXTRA_REQUEST_PRICE

        )





        usage_billing = self.repository.get_by_month(

            db,

            organization_id,

            month

        )





        data = {


            "total_requests":

                total_requests,


            "included_requests":

                included_requests,


            "extra_requests":

                extra_requests,


            "cost":

                cost

        }





        if usage_billing:


            return self.repository.update(

                db,

                usage_billing,

                data

            )





        usage_billing = UsageBilling(

            organization_id=organization_id,

            month=month,

            **data

        )





        return self.repository.create(

            db,

            usage_billing

        )