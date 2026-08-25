from .reasoning_engine import ReasoningEngine



class MemoryReasoningEngine:
    """
    ASEO Cognitive Memory Reasoning Adapter

    Shared Memory Intelligence Layer
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


        from ai_engine.cognition import CognitiveOrchestrator


        self.cognitive = CognitiveOrchestrator(
            memory=self.memory
        )





    def analyze(
        self,
        requirement
    ):


        cognitive_result = self.cognitive.analyze(

            requirement

        )



        memories = self.memory.recall(

            requirement

        )



        reasoning_data = {}


        reasoning = cognitive_result.get(
            "reasoning",
            []
        )


        if isinstance(
            reasoning,
            list
        ):

            if reasoning:

                reasoning_data = reasoning[-1]


        elif isinstance(
            reasoning,
            dict
        ):

            reasoning_data = reasoning


        elif isinstance(
            reasoning,
            str
        ):

            reasoning_data = {

                "reasoning":
                    reasoning

            }




        decision = {


            "action":

                reasoning_data.get(

                    "action",

                    cognitive_result.get(

                        "action",

                        "No decision generated"

                    )

                ),



            "confidence":

                cognitive_result.get(

                    "confidence",

                    0

                ),



            "reasoning":

                reasoning_data.get(

                    "reasoning",

                    ""

                ),



            "patterns":

                cognitive_result.get(

                    "patterns",

                    []

                ),



            "evidence":

                cognitive_result.get(

                    "evidence",

                    []

                )

        }




        return {


            "decision":

                decision,


            "memory_used":

                memories,


            "patterns":

                cognitive_result.get(

                    "patterns",

                    []

                ),


            "evidence":

                cognitive_result.get(

                    "evidence",

                    []

                ),


            "cognitive_confidence":

                cognitive_result.get(

                    "confidence",

                    0

                )

        }