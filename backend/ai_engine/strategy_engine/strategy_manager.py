from .opportunity_analyzer import OpportunityAnalyzer

from .roi_calculator import ROICalculator

from .risk_analyzer import RiskAnalyzer

from .strategy_planner import StrategyPlanner




class StrategyManager:
    """
    ASEO Autonomous Strategy Engine v21.8
    """

    def __init__(self):

        self.opportunity = OpportunityAnalyzer()

        self.roi = ROICalculator()

        self.risk = RiskAnalyzer()

        self.planner = StrategyPlanner()



    def evaluate(
        self,
        idea
    ):


        opportunity = self.opportunity.analyze(

            idea

        )


        roi = self.roi.calculate(

            opportunity

        )


        risk = self.risk.analyze(

            opportunity

        )


        strategy = self.planner.plan(

            idea,

            roi,

            risk

        )


        return {

            "opportunity":
                opportunity,

            "roi":
                roi,

            "risk":
                risk,

            "strategy":
                strategy

        }