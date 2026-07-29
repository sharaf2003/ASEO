from .agent_profile import AgentProfile

from .agent_registry import AgentRegistry

from .agent_selector import AgentSelector

from .agent_cost import AgentCost




class MarketplaceManager:
    """
    ASEO Agent Marketplace v22.7
    """

    def __init__(self):

        self.profile = AgentProfile()

        self.registry = AgentRegistry()

        self.selector = AgentSelector()

        self.cost = AgentCost()



    def build_team(
        self
    ):


        agents = [

            self.profile.create(
                "backend_engineer",
                "Backend Engineer",
                [
                    "FastAPI",
                    "Python"
                ]
            ),


            self.profile.create(
                "database_engineer",
                "Database Engineer",
                [
                    "PostgreSQL",
                    "SQL"
                ]
            ),


            self.profile.create(
                "security_engineer",
                "Security Engineer",
                [
                    "Security",
                    "Authentication"
                ]
            )

        ]


        for agent in agents:

            self.registry.register(

                agent

            )


        selection = self.selector.select(

            agents,

            "FastAPI"

        )


        cost = self.cost.calculate(

            selection["selected"]

        )


        return {

            "agents":
                self.registry.list_agents(),

            "selection":
                selection,

            "cost":
                cost,

            "status":
                "team_ready"

        }