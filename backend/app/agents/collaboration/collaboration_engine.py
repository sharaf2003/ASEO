class CollaborationEngine:


    def __init__(self):

        self.messages = []



    def send(

        self,

        sender: str,

        receiver: str,

        message_type: str,

        content: dict

    ):


        message = {

            "sender": sender,

            "receiver": receiver,

            "type": message_type,

            "content": content

        }


        self.messages.append(

            message

        )


        return message



    def get_messages_for(

        self,

        receiver: str

    ):


        return [

            message

            for message in self.messages

            if message["receiver"] == receiver

        ]