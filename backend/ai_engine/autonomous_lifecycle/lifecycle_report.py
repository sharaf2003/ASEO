from datetime import datetime
from uuid import uuid4



class LifecycleReport:
    """
    ASEO Lifecycle Report v17.6
    """



    def __init__(
        self,
        project,
        status,
        stages
    ):


        self.id = str(uuid4())

        self.project = project

        self.status = status

        self.stages = stages

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