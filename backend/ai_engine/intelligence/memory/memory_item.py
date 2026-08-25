from dataclasses import dataclass
from datetime import datetime




@dataclass
class MemoryItem:
    """
    ASEO Memory Item v14

    Long Term Engineering Memory Unit

    Supports:
    - Deduplication
    - Usage Tracking
    - Confidence Evolution
    """


    key: str

    value: str

    category: str = "general"

    confidence: float = 1.0


    created_at: datetime = None


    usage_count: int = 0

    success_count: int = 0


    last_used: datetime = None



    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.utcnow()



    def reinforce(
        self,
        confidence_boost=0.02
    ):

        """
        Called when existing memory is reused.
        """

        self.usage_count += 1


        self.confidence = min(

            1.0,

            self.confidence + confidence_boost

        )


        self.last_used = datetime.utcnow()



    def mark_success(self):

        self.success_count += 1



        self.confidence = min(

            1.0,

            self.confidence + 0.03

        )



    def to_dict(self):

        return {

            "key":
                self.key,


            "value":
                self.value,


            "category":
                self.category,


            "confidence":
                round(
                    self.confidence,
                    3
                ),


            "usage_count":
                self.usage_count,


            "success_count":
                self.success_count,


            "created_at":
                self.created_at.isoformat(),


            "last_used":
                self.last_used.isoformat()
                if self.last_used
                else None

        }