from dataclasses import dataclass



@dataclass
class Decision:
    """
    ASEO Decision Object v13
    """

    action: str

    confidence: float

    reasoning: str



    def to_dict(self):

        return {

            "action":
                self.action,

            "confidence":
                self.confidence,

            "reasoning":
                self.reasoning

        }