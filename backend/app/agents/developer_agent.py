from app.agents.base_agent import BaseAgent

from app.agents.capabilities import AgentCapability

from app.shared.models.execution import ExecutionContext

from app.shared.models.artifact import Artifact



class DeveloperAgent(BaseAgent):

    """
    Responsible for converting
    architecture into implementation tasks
    and development artifacts.
    """



    name = "DeveloperAgent"

    role = "developer"



    description = (
        "Transforms architecture designs into "
        "implementation plans and software "
        "development tasks."
    )



    capabilities = [

        AgentCapability.BACKEND_DEVELOPMENT,

        AgentCapability.FRONTEND_DEVELOPMENT,

        AgentCapability.API_DEVELOPMENT,

        AgentCapability.DATABASE_IMPLEMENTATION,

        AgentCapability.CODE_GENERATION

    ]



    def run(

        self,

        context: ExecutionContext

    ) -> dict:



        # =========================================
        # Create Main Development Task
        # =========================================

        main_task = context.create_task(

            name="Develop application",

            agent_name=self.name,

            description=(

                "Implement the application "
                "based on approved architecture."

            )

        )


        context.start_task(main_task)



        try:


            # =========================================
            # Get Architecture Result
            # =========================================

            architecture_result = context.metadata.get(

                "architecture_result",

                {}

            )



            architecture = architecture_result.get(

                "architecture",

                {}

            )



            if not architecture:

                raise ValueError(

                    "Architecture is required "
                    "before development phase"

                )



            # =========================================
            # Create Development Sub Tasks
            # =========================================

            development_tasks = [

                "Create backend models",

                "Create repositories",

                "Create service layer",

                "Create API endpoints",

                "Create frontend components"

            ]



            created_tasks = []



            for task_name in development_tasks:


                task = context.create_task(

                    name=task_name,

                    agent_name=self.name,

                    description=task_name

                )


                context.start_task(task)



                context.complete_task(

                    task,

                    {

                        "result": "planned",

                        "task": task_name

                    }

                )


                created_tasks.append(task_name)



            # =========================================
            # Create Development Artifact
            # =========================================

            implementation_plan = {


                "backend": [

                    "Create database models",

                    "Create repositories",

                    "Create service layer",

                    "Create API endpoints"

                ],


                "frontend": [

                    "Create UI components",

                    "Create application pages",

                    "Integrate APIs"

                ],


                "testing": [

                    "Write unit tests",

                    "Run integration tests"

                ]

            }



            artifact = Artifact(

                execution_id=context.id,

                created_by_agent=self.name,

                artifact_type="IMPLEMENTATION_PLAN",

                name="Development Implementation Plan",

                content=implementation_plan

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


                "implementation": implementation_plan,


                "tasks_created": len(created_tasks),


                "based_on": architecture

            }



            context.metadata[

                "development_result"

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