class PerformanceStore:
    """
    ASEO Performance Storage v19.2
    """



    def __init__(
        self
    ):

        self.agents = {}





    def save(
        self,
        profile
    ):


        self.agents[

            profile.agent_name

        ] = profile



        return profile






    def get(
        self,
        name
    ):


        return self.agents.get(

            name

        )





    def all(
        self
    ):


        return [

            agent.to_dict()

            for agent

            in self.agents.values()

        ]