from app.agents.base_agent import BaseAgent

from app.shared.models.execution import ExecutionContext

from app.shared.models.task import Task

from app.shared.models.artifact import Artifact



class DeveloperAgent(BaseAgent):

    """
    Responsible for converting
    architecture into implementation tasks
    and development artifacts.
    """


    name = "DeveloperAgent"

    role = "developer"



    def run(

        self,

        context: ExecutionContext

    ) -> dict:


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
        # Create Development Tasks
        # =========================================

        development_tasks = [


            Task(

                name="Create backend models",

                description="Create database models",

                agent_name=self.name

            ),


            Task(

                name="Create repositories",

                description="Create repository layer",

                agent_name=self.name

            ),


            Task(

                name="Create service layer",

                description="Create business services",

                agent_name=self.name

            ),


            Task(

                name="Create API endpoints",

                description="Create REST API endpoints",

                agent_name=self.name

            ),


            Task(

                name="Create frontend components",

                description="Build frontend interfaces",

                agent_name=self.name

            )


        ]



        for task in development_tasks:

            context.add_task(

                task

            )



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



        # =========================================
        # Save Result
        # =========================================

        result = {


            "agent": self.name,

            "role": self.role,

            "implementation": implementation_plan,

            "tasks_created": len(development_tasks),

            "based_on": architecture

        }



        context.metadata[

            "development_result"

        ] = result



        return result