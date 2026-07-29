from .reasoning_engine import ReasoningEngine



class MemoryReasoningEngine:
    """
    ASEO Memory Enhanced Reasoning v13

    Combines memory knowledge
    with reasoning decisions.
    """



    def __init__(
        self,
        memory,
        reasoning=None
    ):


        self.memory = memory


        self.reasoning = (

            reasoning

            if reasoning

            else ReasoningEngine()

        )





    def analyze(
        self,
        requirement
    ):


        memories = self.memory.recall(

            requirement

        )



        decision = self.reasoning.analyze(

            requirement

        )



        return {


            "decision":

                decision.to_dict(),



            "memory_used":

                memories

        }