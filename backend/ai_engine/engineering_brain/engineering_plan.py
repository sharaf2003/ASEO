from datetime import datetime
from uuid import uuid4



class EngineeringPlan:
    """
    ASEO Engineering Plan v16
    """



    def __init__(
        self,
        requirement
    ):

        self.id = str(uuid4())


        self.requirement = requirement


        self.domain = None


        self.complexity = None


        self.risks = []


        self.steps = []


        self.created_at = datetime.now().isoformat()





    def to_dict(self):

        return {

            "id":
                self.id,


            "requirement":
                self.requirement,


            "domain":
                self.domain,


            "complexity":
                self.complexity,


            "risks":
                self.risks,


            "steps":
                self.steps,


            "created_at":
                self.created_at

        }