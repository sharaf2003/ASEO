from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4



@dataclass
class AgentMessage:
    """
    ASEO Agent Communication Message v13
    """

    sender: str

    receiver: str

    message_type: str

    data: dict



    def __post_init__(self):

        self.id = str(uuid4())

        self.timestamp = datetime.utcnow()



    def to_dict(self):

        return {

            "id":
                self.id,


            "sender":
                self.sender,


            "receiver":
                self.receiver,


            "message_type":
                self.message_type,


            "data":
                self.data,


            "timestamp":
                self.timestamp.isoformat()

        }