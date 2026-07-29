from .market_analyzer import (
    MarketAnalyzer
)

from .customer_analyzer import (
    CustomerAnalyzer
)

from .marketing_strategy import (
    MarketingStrategy
)




class CMOAgent:
    """
    ASEO Autonomous CMO Agent v20.7
    """



    def __init__(self):

        self.market = MarketAnalyzer()

        self.customer = CustomerAnalyzer()

        self.strategy = MarketingStrategy()





    def analyze_growth(
        self,
        product
    ):


        market = self.market.analyze(

            product

        )


        customer = self.customer.analyze(

            product

        )


        strategy = self.strategy.create(

            market,

            customer

        )


        decision = (

            "Launch Campaign"

            if market["opportunity"] == "high"

            else

            "Research More"

        )


        return {


            "market":

                market,


            "customer":

                customer,


            "strategy":

                strategy,


            "decision":

                decision

        }