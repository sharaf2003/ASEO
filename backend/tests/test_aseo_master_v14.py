from ai_engine.master import (
    ASEOMasterEngine
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





aseo = ASEOMasterEngine(

    {

        "planning":
            PlanningAgent(),


        "coding":
            CodingAgent()

    }

)



result = aseo.build(

    "Build ecommerce platform"

)



print(result)