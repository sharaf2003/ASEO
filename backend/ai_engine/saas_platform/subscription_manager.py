from uuid import uuid4


class SubscriptionManager:
    """
    ASEO Subscription Manager v22.5
    """

    def subscribe(
        self,
        customer,
        plan
    ):

        return {

            "id":
                str(uuid4()),

            "customer":
                customer["company"],

            "plan":
                plan,

            "status":
                "active"

        }