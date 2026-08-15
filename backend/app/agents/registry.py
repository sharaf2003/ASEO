from app.agents.planner_agent import PlannerAgent
from app.agents.architect_agent import ArchitectAgent
from app.agents.developer_agent import DeveloperAgent
from app.agents.tester_agent import TesterAgent
from app.agents.deployment_agent import DeploymentAgent



class AgentRegistry:

    """
    Central registry for ASEO agents.

    Responsible for:

    - Registering agents
    - Discovering agents
    - Matching capabilities
    - Managing agent availability
    - Providing runtime dependencies
    """



    def __init__(

        self,

        db=None,

        project_id: int | None = None,

        organization_id: int | None = None

    ):


        self.db = db

        self.project_id = project_id

        self.organization_id = organization_id


        self.agents = {}


        self.register_default_agents()



    # =============================================
    # Register Agents
    # =============================================


    def register(

        self,

        agent

    ):


        if not agent:

            raise ValueError(

                "Agent instance is required"

            )



        if not getattr(agent, "name", None):

            raise ValueError(

                "Agent name is required"

            )



        if not hasattr(agent, "capabilities"):

            raise ValueError(

                f"{agent.name} must define capabilities"

            )


        self.agents[

            agent.name

        ] = agent



    # =============================================
    # Default Agents
    # =============================================


    def register_default_agents(self):


        self.register(

            PlannerAgent(

                db=self.db,

                project_id=self.project_id,

                organization_id=self.organization_id

            )

        )



        self.register(

            ArchitectAgent(

                db=self.db,

                project_id=self.project_id,

                organization_id=self.organization_id

            )

        )



        self.register(

            DeveloperAgent(

                db=self.db,

                project_id=self.project_id,

                organization_id=self.organization_id

            )

        )



        self.register(

            TesterAgent(

                db=self.db,

                project_id=self.project_id,

                organization_id=self.organization_id

            )

        )



        self.register(

            DeploymentAgent(

                db=self.db,

                project_id=self.project_id,

                organization_id=self.organization_id

            )

        )



    # =============================================
    # Get Agent
    # =============================================


    def get_agent(

        self,

        name: str

    ):


        agent = self.agents.get(

            name

        )


        if not agent:

            raise ValueError(

                f"Agent '{name}' is not registered"

            )


        return agent



    # =============================================
    # Find By Capability
    # =============================================


    def find_by_capability(

        self,

        capability

    ):


        results = []



        requested_capability = (

            capability.value

            if hasattr(capability, "value")

            else capability

        )



        for agent in self.agents.values():


            agent_capabilities = [

                item.value

                if hasattr(item, "value")

                else item

                for item in agent.capabilities

            ]


            if requested_capability in agent_capabilities:


                results.append(

                    agent

                )


        return results



    # =============================================
    # Check Agent Exists
    # =============================================


    def has_agent(

        self,

        name: str

    ) -> bool:


        return name in self.agents



    # =============================================
    # List Agents
    # =============================================


    def list_agents(self):


        return list(

            self.agents.values()

        )



    # =============================================
    # List Capabilities
    # =============================================


    def list_capabilities(self):


        capabilities = set()



        for agent in self.agents.values():


            for capability in agent.capabilities:


                value = (

                    capability.value

                    if hasattr(capability, "value")

                    else capability

                )


                capabilities.add(

                    value

                )


        return list(

            capabilities

        )