from app.agents.base_agent import BaseAgent



class PlannerAgent(BaseAgent):


    """
    Responsible for analyzing
    user requirements and creating
    execution tasks.
    """



    def run(

        self,

        context: dict

    ) -> dict:


        request = context.get(
            "request"
        )


        return {


            "agent":

                "PlannerAgent",


            "request":

                request,


            "tasks": [

                {
                    "id": 1,
                    "name": "Analyze requirements",
                    "status": "PENDING"
                },


                {
                    "id": 2,
                    "name": "Design architecture",
                    "status": "PENDING"
                },


                {
                    "id": 3,
                    "name": "Create database schema",
                    "status": "PENDING"
                },


                {
                    "id": 4,
                    "name": "Develop application",
                    "status": "PENDING"
                },


                {
                    "id": 5,
                    "name": "Deploy application",
                    "status": "PENDING"
                }

            ]

        }