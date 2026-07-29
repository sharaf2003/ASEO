from .message import AgentMessage



class CollaborationWorkflow:
    """
    ASEO Agent Workflow Engine v13
    """



    def __init__(self):

        self.agents = {}



    def register_agent(
        self,
        name,
        agent
    ):

        self.agents[name] = agent





    def process(
        self,
        message
    ):


        receiver = self.agents.get(

            message.receiver

        )



        if not receiver:

            return {

                "status":
                    "failed",

                "message":
                    "Agent not found"

            }



        result = receiver.execute(

            message.data

        )



        return {

            "status":
                "completed",

            "agent":
                message.receiver,

            "result":
                result

        }