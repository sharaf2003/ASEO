from .customer_manager import CustomerManager

from .workspace_manager import WorkspaceManager

from .subscription_manager import SubscriptionManager

from .usage_tracker import UsageTracker

from .billing_engine import BillingEngine




class SaaSManager:
    """
    ASEO Autonomous SaaS Platform v22.5
    """

    def __init__(self):

        self.customer = CustomerManager()

        self.workspace = WorkspaceManager()

        self.subscription = SubscriptionManager()

        self.usage = UsageTracker()

        self.billing = BillingEngine()



    def onboard(
        self,
        company,
        plan
    ):


        customer = self.customer.create(

            company

        )


        workspace = self.workspace.create(

            customer

        )


        subscription = self.subscription.subscribe(

            customer,

            plan

        )


        usage = self.usage.track(

            0,

            0

        )


        invoice = self.billing.calculate(

            plan,

            usage

        )


        return {

            "customer":
                customer,

            "workspace":
                workspace,

            "subscription":
                subscription,

            "usage":
                usage,

            "billing":
                invoice,

            "status":
                "onboarded"

        }