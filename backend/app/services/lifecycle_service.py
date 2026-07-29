from sqlalchemy.orm import Session

from app.models.project import Project



class LifecycleService:
    """
    Manages ASEO project lifecycle states.
    """



    def update_status(
        self,
        db: Session,
        project: Project,
        status: str
    ):


        project.status = status


        db.commit()

        db.refresh(project)


        return project