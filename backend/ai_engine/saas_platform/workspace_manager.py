from uuid import uuid4


class WorkspaceManager:
    """
    ASEO Workspace Manager v22.5
    """

    def create(
        self,
        customer
    ):

        return {

            "id":
                str(uuid4()),

            "workspace":
                "Main Workspace",

            "customer":
                customer["company"],

            "status":
                "active"

        }