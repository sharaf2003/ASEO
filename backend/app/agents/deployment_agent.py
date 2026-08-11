from app.agents.base_agent import BaseAgent

from app.shared.models.execution import ExecutionContext

from app.shared.models.task import Task

from app.shared.models.artifact import Artifact



class DeploymentAgent(BaseAgent):

    """
    Responsible for preparing
    deployment strategy and producing
    deployment artifacts.
    """


    name = "DeploymentAgent"

    role = "deployment"



    def run(

        self,

        context: ExecutionContext

    ) -> dict:


        # =========================================
        # Validate Testing Phase
        # =========================================

        testing_result = context.metadata.get(

            "testing_result",

            {}

        )


        if not testing_result:

            raise ValueError(

                "Testing result is required "
                "before deployment phase"

            )



        # =========================================
        # Create Deployment Tasks
        # =========================================

        deployment_tasks = [


            Task(

                name="Prepare Docker configuration",

                description=(
                    "Create containerization "
                    "configuration."
                ),

                agent_name=self.name

            ),


            Task(

                name="Configure CI/CD pipeline",

                description=(
                    "Create automated deployment "
                    "workflow."
                ),

                agent_name=self.name

            ),


            Task(

                name="Configure hosting",

                description=(
                    "Prepare cloud deployment "
                    "environment."
                ),

                agent_name=self.name

            ),


            Task(

                name="Verify health checks",

                description=(
                    "Validate service availability "
                    "after deployment."
                ),

                agent_name=self.name

            )

        ]



        for task in deployment_tasks:

            context.add_task(

                task

            )



        # =========================================
        # Create Deployment Artifact
        # =========================================

        deployment_plan = {


            "environment": "Production",


            "containerization": "Docker",


            "ci_cd": "GitHub Actions",


            "hosting": "Cloud Platform",


            "health_checks": [

                "API availability",

                "Database connection",

                "Service monitoring"

            ]

        }



        artifact = Artifact(

            execution_id=context.id,

            created_by_agent=self.name,

            artifact_type="DEPLOYMENT_PLAN",

            name="Deployment Strategy",

            content=deployment_plan

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

            "deployment": deployment_plan,

            "tasks_created": len(deployment_tasks),

            "status": "READY_TO_DEPLOY"

        }



        context.metadata[

            "deployment_result"

        ] = result



        return result