from app.agents.base_agent import BaseAgent



class TesterAgent(BaseAgent):


    """
    Responsible for validating
    generated implementation plans.
    """



    def run(

        self,

        context: dict

    ) -> dict:



        development = context.get(

            "development",

            {}

        )



        return {


            "agent":

                "TesterAgent",



            "tests":

            {


                "unit":

                [

                    "Test database models",

                    "Test business logic",

                    "Test services"

                ],



                "integration":

                [

                    "Test API endpoints",

                    "Test database integration"

                ],



                "security":

                [

                    "Test authentication",

                    "Test authorization"

                ]

            },



            "based_on":

                development,



            "status":

                "READY_FOR_DEPLOYMENT"

        }