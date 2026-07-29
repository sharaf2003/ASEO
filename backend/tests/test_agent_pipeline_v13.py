from ai_engine.collaboration import (
    AgentPipeline
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





pipeline = AgentPipeline()



pipeline.add_stage(

    "planning",

    PlanningAgent()

)



pipeline.add_stage(

    "coding",

    CodingAgent()

)




result = pipeline.run(

    {

        "project":
            "Ecommerce"

    }

)



print(result)