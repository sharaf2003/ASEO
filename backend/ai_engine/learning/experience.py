from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4



@dataclass
class Experience:
    """
    ASEO Experience Object v14

    Stores project execution knowledge.
    """

    project: str

    decision: dict

    result: dict

    success: bool

    score: float = 0.0



    def __post_init__(self):

        self.id = str(uuid4())

        self.created_at = datetime.utcnow()



    def to_dict(self):

        return {

            "id":
                self.id,

            "project":
                self.project,

            "decision":
                self.decision,

            "result":
                self.result,

            "success":
                self.success,

            "score":
                self.score,

            "created_at":
                self.created_at.isoformat()

        }