from ai_engine.memory_intelligence import (
    MemoryRetriever
)

from .decision_analyzer import (
    DecisionAnalyzer
)



class ArchitectureDecisionEngine:
    """
    ASEO Architecture Decision Engine v14
    """



    def __init__(self):

        self.memory = MemoryRetriever()

        self.analyzer = DecisionAnalyzer()





    def decide(
        self,
        requirement
    ):


        memories = self.memory.retrieve(

            requirement

        )


        recommendation = self.analyzer.analyze(

            memories

        )



        return {


            "requirement":

                requirement,


            "recommendation":

                recommendation,


            "confidence":

                0.98 if recommendation else 0.5,


            "based_on_knowledge":

                bool(recommendation)

        }