from datetime import datetime
from uuid import uuid4



class EngineeringMemory:
    """
    ASEO Engineering Memory v16.6
    """



    def __init__(
        self,
        project,
        decision,
        result
    ):

        self.id = str(uuid4())

        self.project = project

        self.decision = decision

        self.result = result

        self.created_at = datetime.now().isoformat()



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
                self.created_at

        }