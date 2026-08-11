from app.agents.base_agent import BaseAgent

from app.shared.models.execution import ExecutionContext
from app.shared.models.task import Task


class PlannerAgent(BaseAgent):

    """
    Responsible for analyzing user requirements
    and creating the initial execution tasks.
    """

    name = "PlannerAgent"

    role = "planner"


    # =====================================================
    # Run Planner
    # =====================================================

    def run(

        self,

        context: ExecutionContext

    ) -> dict:

        """
        Analyze the execution request and create
        the initial ASEO engineering task plan.
        """

        request = context.metadata.get(
            "request"
        )


        if not request:

            raise ValueError(
                "Execution request is required "
                "for PlannerAgent"
            )


        # =================================================
        # Create Planning Tasks
        # =================================================

        tasks = [

            Task(

                name="Analyze requirements",

                description=(
                    "Analyze the user request and "
                    "identify functional and technical "
                    "requirements."
                ),

                agent_name="PlannerAgent",

                input_data={
                    "request": request
                }

            ),


            Task(

                name="Design architecture",

                description=(
                    "Design the software architecture "
                    "based on the analyzed requirements."
                ),

                agent_name="ArchitectAgent"

            ),


            Task(

                name="Create database schema",

                description=(
                    "Design the required database "
                    "schema and relationships."
                ),

                agent_name="ArchitectAgent"

            ),


            Task(

                name="Develop application",

                description=(
                    "Implement the application based "
                    "on the approved architecture."
                ),

                agent_name="DeveloperAgent"

            ),


            Task(

                name="Test application",

                description=(
                    "Validate the generated application "
                    "using unit, integration and "
                    "security tests."
                ),

                agent_name="TesterAgent"

            ),


            Task(

                name="Deploy application",

                description=(
                    "Prepare and execute the deployment "
                    "workflow."
                ),

                agent_name="DeploymentAgent"

            )

        ]


        # =================================================
        # Attach Tasks To Execution Context
        # =================================================

        for task in tasks:

            context.add_task(
                task
            )


        # =================================================
        # Store Planner Result
        # =================================================

        planner_result = {

            "agent": self.name,

            "role": self.role,

            "request": request,

            "tasks_created": len(tasks),

            "tasks": [

                {

                    "name": task.name,

                    "description": task.description,

                    "agent": task.agent_name,

                    "status": task.status.value

                }

                for task in tasks

            ]

        }


        context.metadata[
            "planner_result"
        ] = planner_result


        return planner_result