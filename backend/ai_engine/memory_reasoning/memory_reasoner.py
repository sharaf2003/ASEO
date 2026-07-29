from ai_engine.memory_intelligence import (
    MemoryRetriever
)

from .decision_fusion import (
    DecisionFusion
)



class MemoryReasoner:
    """
    ASEO Memory Driven Reasoning v14
    """



    def __init__(
        self,
        reasoning
    ):


        self.reasoning = reasoning

        self.memory = MemoryRetriever()

        self.fusion = DecisionFusion()





    def analyze(
        self,
        requirement
    ):


        memories = self.memory.retrieve(

            requirement

        )


        decision = self.reasoning.analyze(

            requirement

        )



        result = decision.to_dict()



        result = self.fusion.combine(

            result,

            memories

        )


        return {

            "decision":
                result,

            "memory_used":
                memories

        }