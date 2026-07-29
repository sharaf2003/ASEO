from dataclasses import dataclass
from datetime import datetime



@dataclass
class AgentScore:
    """
    ASEO Agent Performance Score v14
    """

    agent: str

    executions: int = 0

    successful: int = 0

    failed: int = 0

    quality_score: float = 0.0



    created_at: datetime = None



    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.utcnow()





    @property
    def success_rate(self):

        if self.executions == 0:

            return 0


        return round(

            (self.successful / self.executions) * 100,

            2

        )





    def to_dict(self):

        return {

            "agent":
                self.agent,


            "executions":
                self.executions,


            "successful":
                self.successful,


            "failed":
                self.failed,


            "success_rate":
                self.success_rate,


            "quality_score":
                self.quality_score,


            "created_at":
                self.created_at.isoformat()

        }