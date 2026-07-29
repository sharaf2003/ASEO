from ai_engine.orchestrator import (
    AutonomousExecutionEngine
)



class ASEOEngine:
    """
    ASEO Main Engine v13

    Public interface for
    autonomous software engineering.
    """



    def __init__(
        self,
        agents=None
    ):


        self.engine = AutonomousExecutionEngine(

            agents

        )





    def build_project(
        self,
        requirement
    ):


        result = self.engine.run(

            requirement

        )


        return {


            "status":

                result.get(

                    "status",

                    "failed"

                ),


            "project":

                requirement,


            "execution":

                result


        }