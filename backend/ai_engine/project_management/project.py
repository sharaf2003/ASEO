from datetime import datetime
from uuid import uuid4



class Project:
    """
    ASEO Project Entity v19.3
    """



    def __init__(
        self,
        name,
        client
    ):


        self.id = str(uuid4())

        self.name = name

        self.client = client

        self.status = "created"

        self.team = []

        self.quality = None

        self.created_at = datetime.now()





    def assign_team(
        self,
        team
    ):


        self.team = team





    def update_status(
        self,
        status
    ):


        self.status = status





    def set_quality(
        self,
        score
    ):


        self.quality = score






    def to_dict(
        self
    ):


        return {


            "id":

                self.id,


            "project":

                self.name,


            "client":

                self.client,


            "status":

                self.status,


            "team":

                self.team,


            "quality":

                self.quality,


            "created_at":

                self.created_at.isoformat()

        }