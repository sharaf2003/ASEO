from app.agents.planner_agent import PlannerAgent

from app.agents.architect_agent import ArchitectAgent

from app.agents.developer_agent import DeveloperAgent

from app.agents.tester_agent import TesterAgent

from app.agents.deployment_agent import DeploymentAgent




class AgentOrchestrator:


    """
    Controls execution flow between ASEO agents.

    Pipeline:

    Planner
        |
    Architect
        |
    Developer
        |
    Tester
    """



    def __init__(self):


        self.planner = PlannerAgent()


        self.architect = ArchitectAgent()


        self.developer = DeveloperAgent()


        self.tester = TesterAgent()

        self.deployment = DeploymentAgent()





    def run(

        self,

        request: str

    ) -> dict:



        # =====================
        # Planning
        # =====================


        plan = self.planner.run(

            {

                "request": request

            }

        )



        # =====================
        # Architecture
        # =====================


        architecture = self.architect.run(

            plan

        )



        # =====================
        # Development
        # =====================


        development = self.developer.run(

            architecture

        )



        # =====================
        # Testing
        # =====================


        testing = self.tester.run(

            {

                "development": development

            }

        )

        deployment = self.deployment.run(

            {
                "testing": testing
            }

        )



        return {


            "plan": plan,


            "architecture": architecture,


            "development": development,


            "testing": testing,

            "deployment": deployment

        }