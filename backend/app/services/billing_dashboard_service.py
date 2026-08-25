from sqlalchemy.orm import Session


from app.services.subscription_service import (
    SubscriptionService
)


from app.services.billing_service import (
    BillingService
)


from app.services.usage_billing_service import (
    UsageBillingService
)





class BillingDashboardService:

    """
    ASEO Customer Billing Dashboard Service.
    """



    def __init__(self):

        self.subscription_service = SubscriptionService()

        self.billing_service = BillingService()

        self.usage_service = UsageBillingService()





    # =====================================
    # Get Billing Dashboard
    # =====================================


    def get_dashboard(

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





        usage = self.usage_service.calculate_monthly_usage(

            db,

            organization_id,

            month

        )





        invoices = self.billing_service.get_invoices(

            db,

            organization_id

        )





        return {


            "subscription": subscription,


            "limits": limits,


            "usage": usage,


            "invoices": invoices

        }