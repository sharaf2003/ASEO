from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4



@dataclass
class CompanyExperience:
    """
    ASEO Company Experience v19.1
    """

    project: str

    decision: str

    result: dict



    def __post_init__(self):

        self.id = str(uuid4())

        self.created_at = datetime.now()



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

            "created_at":
                self.created_at.isoformat()

        }