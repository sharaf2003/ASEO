from app.agents.base_agent import BaseAgent



class ArchitectAgent(BaseAgent):


    """
    Responsible for designing
    system architecture.
    """



    def run(

        self,

        context: dict

    ) -> dict:



        tasks = context.get(
            "tasks",
            []
        )


        architecture = {


            "backend": {

                "technology": "FastAPI",

                "architecture": "REST API"

            },


            "database": {

                "technology": "PostgreSQL",

                "orm": "SQLAlchemy"

            },


            "frontend": {

                "technology": "React",

                "type": "SPA"

            },


            "deployment": {

                "technology": "Docker",

                "environment": "Cloud"

            }

        }



        return {


            "agent":

                "ArchitectAgent",


            "input_tasks":

                tasks,


            "architecture":

                architecture

        }