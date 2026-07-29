from ai_engine.autonomous_learning import (
    AutonomousLearningEngine
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





engine = AutonomousLearningEngine(

    {

        "planning":
            PlanningAgent(),


        "coding":
            CodingAgent()

    }

)



result = engine.learn_build_project(

    "Build ecommerce backend system"

)



print(result)