from datetime import datetime
from uuid import uuid4



class ProductionReport:
    """
    ASEO Production Report v17.7
    """



    def __init__(
        self,
        project,
        stages
    ):


        self.id = str(uuid4())

        self.project = project

        self.stages = stages

        self.status = "production_ready"

        self.created_at = datetime.now().isoformat()





    def to_dict(
        self
    ):


        return {

            "id":
                self.id,

            "project":
                self.project,

            "status":
                self.status,

            "stages":
                self.stages,

            "created_at":
                self.created_at

        }