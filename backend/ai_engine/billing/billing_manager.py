from .plan import Plan
from .subscription import Subscription




class BillingManager:
    """
    ASEO Billing Manager v19.5
    """



    def __init__(
        self
    ):

        self.plans = {}

        self.subscriptions = {}

        self.usage = {}




    def create_plan(
        self,
        name,
        price,
        max_projects,
        max_agents
    ):


        plan = Plan(

            name,

            price,

            max_projects,

            max_agents

        )


        self.plans[

            plan.id

        ] = plan



        return plan.to_dict()





    def subscribe(
        self,
        customer_id,
        plan_id
    ):


        plan = self.plans.get(

            plan_id

        )


        if not plan:

            return None



        subscription = Subscription(

            customer_id,

            plan

        )


        self.subscriptions[

            subscription.id

        ] = subscription



        self.usage[

            customer_id

        ] = {


            "projects":

                0,


            "agent_tasks":

                0,


            "deployments":

                0

        }



        return subscription.to_dict()





    def track_usage(
        self,
        customer_id,
        metric
    ):


        if customer_id in self.usage:

            if metric in self.usage[customer_id]:

                self.usage[customer_id][metric] += 1



        return self.usage.get(

            customer_id

        )