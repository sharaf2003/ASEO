from datetime import datetime
from uuid import uuid4



class EngineeringDecision:
    """
    ASEO Engineering Decision v16.7
    """



    def __init__(
        self,
        decision,
        confidence,
        reasoning
    ):


        self.id = str(uuid4())


        self.decision = decision


        self.confidence = confidence


        self.reasoning = reasoning


        self.created_at = datetime.now().isoformat()



    def to_dict(self):


        return {

            "id":
                self.id,


            "decision":
                self.decision,


            "confidence":
                self.confidence,


            "reasoning":
                self.reasoning,


            "created_at":
                self.created_at

        }