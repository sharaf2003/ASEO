from app.agents.base_agent import BaseAgent



class DeveloperAgent(BaseAgent):


    """
    Responsible for converting
    architecture into implementation tasks.
    """



    def run(

        self,

        context: dict

    ) -> dict:



        architecture = context.get(

            "architecture",

            {}

        )



        return {


            "agent":

                "DeveloperAgent",



            "implementation":

            {


                "backend":

                [

                    "Create database models",

                    "Create repositories",

                    "Create service layer",

                    "Create API endpoints"

                ],



                "database":

                [

                    "Create schema",

                    "Create migrations",

                    "Create relationships"

                ],



                "frontend":

                [

                    "Create UI components",

                    "Create application pages",

                    "Integrate APIs"

                ],



                "testing":

                [

                    "Write unit tests",

                    "Run integration tests"

                ]

            },



            "based_on":

                architecture

        }