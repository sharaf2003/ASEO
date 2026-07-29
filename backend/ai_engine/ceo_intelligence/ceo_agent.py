from .company_analyzer import (
    CompanyAnalyzer
)

from .priority_manager import (
    PriorityManager
)

from .strategic_engine import (
    StrategicEngine
)



class CEOAgent:
    """
    ASEO Autonomous CEO Agent v20.5
    """



    def __init__(self):

        self.analyzer = CompanyAnalyzer()

        self.priority = PriorityManager()

        self.strategy = StrategicEngine()





    def analyze_company(
        self,
        company_data
    ):


        analysis = self.analyzer.analyze(

            company_data

        )


        priority = self.priority.determine(

            analysis

        )


        decision = self.strategy.decide(

            analysis,

            priority

        )


        return {


            "company_analysis":

                analysis,


            "priority":

                priority,


            "decision":

                decision

        }