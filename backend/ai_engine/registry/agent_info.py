class AgentInfo:
    """
    ASEO Agent Metadata v13
    """


    def __init__(
        self,
        name,
        agent,
        version="1.0"
    ):

        self.name = name

        self.agent = agent

        self.version = version

        self.status = "registered"



    def to_dict(self):

        return {

            "name":
                self.name,

            "version":
                self.version,

            "status":
                self.status

        }