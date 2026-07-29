class BillingEngine:
    """
    ASEO Billing Engine v22.5
    """

    def calculate(
        self,
        plan,
        usage
    ):


        prices = {

            "Starter":99,

            "Professional":199,

            "Enterprise":499

        }


        return {

            "plan":
                plan,

            "amount":
                prices.get(
                    plan,
                    0
                ),

            "usage":
                usage,

            "status":
                "generated"

        }