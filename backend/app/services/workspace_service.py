from sqlalchemy.orm import Session


from app.models.workspace import Workspace


from app.repositories.workspace_repository import (
    WorkspaceRepository
)





class WorkspaceService:
    """
    Service layer for ASEO workspaces.
    """



    def __init__(self):

        self.repository = WorkspaceRepository()





    def create_workspace(

        self,

        db: Session,

        data,

        organization_id: int

    ):


        workspace = Workspace(

            organization_id=organization_id,

            name=data.name

        )



        return self.repository.create(

            db,

            workspace

        )







    def get_organization_workspaces(

        self,

        db: Session,

        organization_id: int

    ):


        return self.repository.get_by_organization(

            db,

            organization_id

        )