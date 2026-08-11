from app.agents.base_agent import BaseAgent

from app.shared.models.execution import ExecutionContext

from app.shared.models.task import Task

from app.shared.models.artifact import Artifact



class TesterAgent(BaseAgent):

    """
    Responsible for validating
    generated implementation plans
    and producing test artifacts.
    """


    name = "TesterAgent"

    role = "tester"



    def run(

        self,

        context: ExecutionContext

    ) -> dict:


        # =========================================
        # Get Development Result
        # =========================================

        development_result = context.metadata.get(

            "development_result",

            {}

        )


        if not development_result:

            raise ValueError(

                "Development result is required "
                "before testing phase"

            )



        # =========================================
        # Create Testing Tasks
        # =========================================

        test_tasks = [


            Task(

                name="Run unit tests",

                description=(
                    "Validate models, services "
                    "and business logic."
                ),

                agent_name=self.name

            ),


            Task(

                name="Run integration tests",

                description=(
                    "Validate API and database "
                    "integration."
                ),

                agent_name=self.name

            ),


            Task(

                name="Run security tests",

                description=(
                    "Validate authentication "
                    "and authorization."
                ),

                agent_name=self.name

            )

        ]



        for task in test_tasks:

            context.add_task(

                task

            )



        # =========================================
        # Create Test Artifact
        # =========================================

        test_plan = {


            "unit": [

                "Test database models",

                "Test business logic",

                "Test services"

            ],


            "integration": [

                "Test API endpoints",

                "Test database integration"

            ],


            "security": [

                "Test authentication",

                "Test authorization"

            ]

        }



        artifact = Artifact(

            execution_id=context.id,

            created_by_agent=self.name,

            artifact_type="TEST_PLAN",

            name="Application Test Plan",

            content=test_plan

        )


        context.add_artifact(

            artifact

        )



        # =========================================
        # Save Result
        # =========================================

        result = {


            "agent": self.name,

            "role": self.role,

            "tests": test_plan,

            "tasks_created": len(test_tasks),

            "status": "READY_FOR_DEPLOYMENT"

        }



        context.metadata[

            "testing_result"

        ] = result



        return result