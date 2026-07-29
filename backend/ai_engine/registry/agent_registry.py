class AgentRegistry:
    """
    ASEO Dynamic Agent Registry v13
    """



    def __init__(self):

        self.agents = {}




    def register(
        self,
        agent_info
    ):


        self.agents[

            agent_info.name

        ] = agent_info




    def get(
        self,
        name
    ):


        return self.agents.get(

            name

        )




    def list_agents(self):


        return [

            agent.to_dict()

            for agent

            in self.agents.values()

        ]