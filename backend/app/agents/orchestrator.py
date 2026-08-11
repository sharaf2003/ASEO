from app.agents.planner_agent import PlannerAgent
from app.agents.architect_agent import ArchitectAgent
from app.agents.developer_agent import DeveloperAgent
from app.agents.tester_agent import TesterAgent
from app.agents.deployment_agent import DeploymentAgent


from app.shared.models.execution import ExecutionContext



class AgentOrchestrator:

    """
    Controls execution flow between ASEO agents.

    Uses ExecutionContext as the shared
    communication layer between agents.
    """


    def __init__(self):

        self.planner = PlannerAgent()

        self.architect = ArchitectAgent()

        self.developer = DeveloperAgent()

        self.tester = TesterAgent()

        self.deployment = DeploymentAgent()



    def run(

        self,

        request: str,

        project_id: int | None = None,

        organization_id: int | None = None

    ) -> dict:


        context = ExecutionContext(

            project_id=project_id,

            organization_id=organization_id,

            metadata={

                "request": request

            }

        )


        try:


            # =====================
            # Planning
            # =====================

            context.start(

                self.planner.name

            )

            self.planner.execute(

                context

            )



            # =====================
            # Architecture
            # =====================

            context.current_agent = (

                self.architect.name

            )

            self.architect.execute(

                context

            )



            # =====================
            # Development
            # =====================

            context.current_agent = (

                self.developer.name

            )

            self.developer.execute(

                context

            )



            # =====================
            # Testing
            # =====================

            context.current_agent = (

                self.tester.name

            )

            self.tester.execute(

                context

            )



            # =====================
            # Deployment
            # =====================

            context.current_agent = (

                self.deployment.name

            )

            self.deployment.execute(

                context

            )


            context.complete()



        except Exception as error:


            context.fail(

                str(error)

            )

            raise



        return {


            "execution_status": (

                context.status.value

            ),


            "project_id": (

                context.project_id

            ),


            "tasks": [

                {

                    "name": task.name,

                    "agent": task.agent_name,

                    "status": task.status.value

                }

                for task in context.tasks

            ],


            "artifacts": [

                {

                    "name": artifact.name,

                    "type": artifact.artifact_type,

                    "agent": artifact.created_by_agent

                }

                for artifact in context.artifacts

            ],


            "metadata": context.metadata

        }