from sqlalchemy.orm import Session

from app.models.workspace import Workspace





class WorkspaceRepository:
    """
    Repository for ASEO workspaces.
    """



    def create(

        self,

        db: Session,

        workspace: Workspace

    ):


        db.add(workspace)

        db.commit()

        db.refresh(workspace)


        return workspace





    def get_by_organization(

        self,

        db: Session,

        organization_id: int

    ):


        return db.query(

            Workspace

        ).filter(

            Workspace.organization_id == organization_id

        ).all()