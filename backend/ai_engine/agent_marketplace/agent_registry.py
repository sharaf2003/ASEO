class AgentRegistry:
    """
    ASEO Agent Registry v22.7
    """

    def __init__(self):

        self.agents = []


    def register(
        self,
        agent
    ):

        self.agents.append(

            agent

        )

        return agent


    def list_agents(
        self
    ):

        return self.agents