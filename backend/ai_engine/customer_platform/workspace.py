from datetime import datetime
from uuid import uuid4



class Workspace:
    """
    ASEO Customer Workspace v19.4
    """



    def __init__(
        self,
        name,
        customer_id
    ):

        self.id = str(uuid4())

        self.name = name

        self.customer_id = customer_id

        self.projects = []

        self.created_at = datetime.now()



    def add_project(
        self,
        project_id
    ):

        self.projects.append(
            project_id
        )



    def dashboard(
        self
    ):

        return {

            "workspace":
                self.name,

            "projects":
                len(self.projects),

            "status":
                "active"

        }



    def to_dict(
        self
    ):

        return {

            "id":
                self.id,

            "workspace":
                self.name,

            "customer_id":
                self.customer_id,

            "projects":
                self.projects,

            "created_at":
                self.created_at.isoformat()

        }