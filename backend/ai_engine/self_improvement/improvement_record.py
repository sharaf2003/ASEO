from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4




@dataclass
class ImprovementRecord:
    """
    ASEO Improvement Record v17.5

    Stores:
    - Prompt improvements
    - Error fixes
    - Engineering improvements
    """



    old_score: float

    new_score: float

    old_prompt: str

    new_prompt: str

    improved: bool


    # New v17.5 fields

    problem: str = None

    solution: str = None

    success: bool = False



    id: str = field(
        init=False
    )


    created_at: datetime = field(
        init=False
    )





    def __post_init__(
        self
    ):


        self.id = str(uuid4())


        self.created_at = datetime.utcnow()





    def add_fix(
        self,
        problem,
        solution,
        success=True
    ):


        self.problem = problem


        self.solution = solution


        self.success = success





    def to_dict(
        self
    ):


        return {


            "id":

                self.id,



            "old_score":

                self.old_score,



            "new_score":

                self.new_score,



            "old_prompt":

                self.old_prompt,



            "new_prompt":

                self.new_prompt,



            "improved":

                self.improved,



            "problem":

                self.problem,



            "solution":

                self.solution,



            "success":

                self.success,



            "created_at":

                self.created_at.isoformat()

        }