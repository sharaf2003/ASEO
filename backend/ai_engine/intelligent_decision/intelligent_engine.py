from .memory_analyzer import (
    MemoryAnalyzer
)

from .experience_ranker import (
    ExperienceRanker
)

from .decision_optimizer import (
    DecisionOptimizer
)




class IntelligentDecisionEngine:
    """
    ASEO Intelligent Decision Engine v20.2
    """



    def __init__(self):

        self.analyzer = MemoryAnalyzer()

        self.ranker = ExperienceRanker()

        self.optimizer = DecisionOptimizer()





    def decide(
        self,
        requirement,
        memories
    ):


        matches = self.analyzer.analyze(

            memories,

            requirement

        )


        ranked = self.ranker.rank(

            matches

        )


        decision = self.optimizer.optimize(

            ranked

        )


        return {


            "requirement":

                requirement,


            "memory_matches":

                len(matches),


            "decision":

                decision

        }