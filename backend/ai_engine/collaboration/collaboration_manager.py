from .message import AgentMessage




class CollaborationManager:
    """
    ASEO Multi Agent Collaboration Manager v13
    """



    def __init__(self):

        self.messages = []




    def send(
        self,
        message
    ):


        self.messages.append(

            message

        )


        return message.to_dict()





    def history(self):


        return [

            message.to_dict()

            for message

            in self.messages

        ]