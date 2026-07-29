from datetime import datetime
from uuid import uuid4



class Event:
    """
    ASEO Event Object v13

    Represents communication message
    between autonomous agents.
    """



    def __init__(
        self,
        event_type,
        agent,
        data=None
    ):


        self.id = str(uuid4())


        self.event_type = event_type


        self.agent = agent


        self.data = data or {}


        self.timestamp = datetime.utcnow()



    def to_dict(self):

        return {

            "id":
                self.id,


            "event_type":
                self.event_type,


            "agent":
                self.agent,


            "data":
                self.data,


            "timestamp":
                self.timestamp.isoformat()

        }