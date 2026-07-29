from .financial_analyzer import (
    FinancialAnalyzer
)

from .cost_optimizer import (
    CostOptimizer
)

from .pricing_engine import (
    PricingEngine
)




class CFOAgent:
    """
    ASEO Autonomous CFO Agent v20.6
    """



    def __init__(self):

        self.analyzer = FinancialAnalyzer()

        self.cost = CostOptimizer()

        self.pricing = PricingEngine()





    def analyze_project(
        self,
        project,
        agents
    ):


        financial = self.analyzer.analyze(

            project

        )


        costs = self.cost.optimize(

            financial["estimated_cost"],

            agents

        )


        pricing = self.pricing.calculate(

            costs["total_cost"]

        )


        decision = (

            "Approve Project"

            if pricing["margin"] >= 40

            else

            "Review Project"

        )


        return {

            "financial_analysis":

                financial,


            "cost_analysis":

                costs,


            "pricing":

                pricing,


            "decision":

                decision

        }