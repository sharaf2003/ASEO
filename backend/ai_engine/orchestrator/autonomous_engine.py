from ai_engine.intelligence.memory import (
    MemoryManager
)

from ai_engine.intelligence.reasoning import (
    MemoryReasoningEngine
)

from ai_engine.collaboration import (
    AgentPipeline
)



class AutonomousExecutionEngine:
    """
    ASEO Autonomous Execution Engine v13

    Complete autonomous project execution layer.
    """



    def __init__(
        self,
        agents=None,
        memory=None
    ):


        self.memory = memory if memory else MemoryManager()


        self.reasoning = MemoryReasoningEngine(

            self.memory

        )


        self.pipeline = AgentPipeline()



        if agents:


            for name, agent in agents.items():


                self.pipeline.add_stage(

                    name,

                    agent

                )





    def run(
        self,
        requirement
    ):


        # Step 1:
        # Analyze requirement using memory + cognition

        intelligence = self.reasoning.analyze(

            requirement

        )





        # Step 2:
        # Prepare execution context

        context = {


            "requirement":

                requirement,



            "decision":

                intelligence["decision"],



            "memory":

                intelligence["memory_used"],



            "patterns":

                intelligence.get(

                    "patterns",

                    []

                ),



            "evidence":

                intelligence.get(

                    "evidence",

                    []

                )

        }





        # Step 3:
        # Execute agents pipeline

        result = self.pipeline.run(

            context

        )





        # Step 4:
        # Preserve evolved intelligence data

        updated_intelligence = {


            **intelligence,



            "patterns":

                result
                .get(
                    "result",
                    {}
                )
                .get(
                    "patterns",
                    intelligence.get(
                        "patterns",
                        []
                    )
                ),



            "evidence":

                result
                .get(
                    "result",
                    {}
                )
                .get(
                    "evidence",
                    intelligence.get(
                        "evidence",
                        []
                    )
                )

        }





        return {


            "status":

                result["status"],



            "intelligence":

                updated_intelligence,



            "execution":

                result

        }