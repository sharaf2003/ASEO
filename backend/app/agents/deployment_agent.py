from app.agents.base_agent import BaseAgent

from app.agents.capabilities import AgentCapability

from app.shared.models.execution import ExecutionContext

from app.shared.models.artifact import Artifact



class DeploymentAgent(BaseAgent):

    """
    Responsible for preparing
    deployment strategy and producing
    deployment artifacts.
    """



    name = "DeploymentAgent"

    role = "deployment"



    description = (
        "Prepares deployment strategies, "
        "CI/CD pipelines and production "
        "deployment configurations."
    )



    capabilities = [

        AgentCapability.DOCKER,

        AgentCapability.CI_CD,

        AgentCapability.CLOUD_DEPLOYMENT,

        AgentCapability.MONITORING

    ]



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
        # Main Deployment Task
        # =========================================

        main_task = context.create_task(

            name="Deploy application",

            agent_name=self.name,

            description=(

                "Prepare and validate "
                "application deployment."

            )

        )


        context.start_task(main_task)



        try:


            # =========================================
            # Deployment Tasks
            # =========================================

            deployment_tasks = [

                "Prepare Docker configuration",

                "Configure CI/CD pipeline",

                "Configure hosting",

                "Verify health checks"

            ]


            completed_tasks = []



            for task_name in deployment_tasks:


                task = context.create_task(

                    name=task_name,

                    agent_name=self.name,

                    description=task_name

                )


                context.start_task(task)



                context.complete_task(

                    task,

                    {

                        "result": "completed",

                        "task": task_name

                    }

                )


                completed_tasks.append(task_name)



            # =========================================
            # Deployment Artifact
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



            result = {


                "agent": self.name,


                "role": self.role,


                "capabilities": [

                    capability.value

                    for capability in self.capabilities

                ],


                "deployment": deployment_plan,


                "tasks_created": len(completed_tasks),


                "status": "READY_TO_DEPLOY"

            }



            context.metadata[

                "deployment_result"

            ] = result



            context.complete_task(

                main_task,

                result

            )



            return result



        except Exception as error:


            context.fail_task(

                main_task,

                str(error)

            )


            raise