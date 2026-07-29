from datetime import datetime
from uuid import uuid4



class Experience:
    """
    ASEO Engineering Experience v16
    """



    def __init__(
        self,
        problem,
        solution,
        success
    ):

        self.id = str(uuid4())

        self.problem = problem

        self.solution = solution

        self.success = success

        self.created_at = datetime.now().isoformat()



    def to_dict(self):

        return {

            "id":
                self.id,

            "problem":
                self.problem,

            "solution":
                self.solution,

            "success":
                self.success,

            "created_at":
                self.created_at

        }