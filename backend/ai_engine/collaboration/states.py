from dataclasses import dataclass
from datetime import datetime



@dataclass
class PipelineState:
    """
    ASEO Pipeline State v13
    """


    stage: str

    agent: str

    status: str = "pending"

    result: dict = None

    timestamp: datetime = None



    def __post_init__(self):

        if self.result is None:

            self.result = {}



        if self.timestamp is None:

            self.timestamp = datetime.utcnow()



    def to_dict(self):

        return {

            "stage":
                self.stage,

            "agent":
                self.agent,

            "status":
                self.status,

            "result":
                self.result,

            "timestamp":
                self.timestamp.isoformat()

        }