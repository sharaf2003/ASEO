from dataclasses import dataclass
from datetime import datetime



@dataclass
class MemoryItem:
    """
    ASEO Memory Item v13
    """


    key: str

    value: str

    category: str = "general"

    confidence: float = 1.0


    created_at: datetime = None



    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.utcnow()



    def to_dict(self):

        return {

            "key":
                self.key,

            "value":
                self.value,

            "category":
                self.category,

            "confidence":
                self.confidence,

            "created_at":
                self.created_at.isoformat()

        }