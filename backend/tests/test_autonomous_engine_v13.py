from ai_engine.orchestrator import (
    AutonomousExecutionEngine
)



class PlanningAgent:


    def execute(
        self,
        context
    ):


        return {

            "architecture":
                "Layered",

            "framework":
                "FastAPI"

        }




class CodingAgent:


    def execute(
        self,
        context
    ):


        return {

            "files":
                10,

            "generated":
                True

        }





engine = AutonomousExecutionEngine(

    {

        "planning":
            PlanningAgent(),


        "coding":
            CodingAgent()

    }

)



result = engine.run(

    "Build ecommerce backend system"

)



print(result)