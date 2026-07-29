from ai_engine.aseo import (
    ASEOEngine
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





aseo = ASEOEngine(

    {

        "planning":
            PlanningAgent(),


        "coding":
            CodingAgent()

    }

)



result = aseo.build_project(

    "Build ecommerce backend system"

)



print(result)