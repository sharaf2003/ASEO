from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4



@dataclass
class PromptVariant:
    """
    ASEO Prompt Variant v14
    """

    original: str

    optimized: str

    score: float = 0.0



    def __post_init__(self):

        self.id = str(uuid4())

        self.created_at = datetime.utcnow()



    def to_dict(self):

        return {

            "id":
                self.id,

            "original":
                self.original,

            "optimized":
                self.optimized,

            "score":
                self.score,

            "created_at":
                self.created_at.isoformat()

        }