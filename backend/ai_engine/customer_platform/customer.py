from datetime import datetime
from uuid import uuid4



class Customer:
    """
    ASEO Customer Entity v19.4
    """

    def __init__(
        self,
        name,
        plan
    ):

        self.id = str(uuid4())

        self.name = name

        self.plan = plan

        self.workspaces = []

        self.created_at = datetime.now()



    def add_workspace(
        self,
        workspace_id
    ):

        self.workspaces.append(
            workspace_id
        )



    def to_dict(
        self
    ):

        return {

            "id":
                self.id,

            "customer":
                self.name,

            "plan":
                self.plan,

            "workspaces":
                self.workspaces,

            "created_at":
                self.created_at.isoformat()

        }