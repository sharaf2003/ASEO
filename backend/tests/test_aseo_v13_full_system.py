from ai_engine.aseo import ASEOEngine



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





class SecurityAgent:


    def execute(
        self,
        context
    ):

        return {

            "security":
                "passed",

            "issues":
                0

        }





aseo = ASEOEngine(

    {

        "planning":
            PlanningAgent(),


        "coding":
            CodingAgent(),


        "security":
            SecurityAgent()

    }

)



result = aseo.build_project(

    "Build ecommerce backend system"

)



validation = {

    "version":
        "13.0",


    "status":
        result["status"],


    "project":
        result["project"],


    "pipeline":
        result["execution"]["execution"]["status"],


    "agents":

        len(

            result["execution"]["execution"]["stages"]

        ),


    "production_ready":

        result["status"] == "completed"

}



print(validation)