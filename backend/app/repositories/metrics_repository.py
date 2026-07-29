from sqlalchemy.orm import Session

from app.models.execution_record import ExecutionRecord

from app.models.project import Project





class MetricsRepository:
    """
    Repository for ASEO metrics collection.
    """



    def get_project(

        self,

        db: Session,

        project_id: int,

        organization_id: int

    ):


        return db.query(

            Project

        ).filter(

            Project.id == project_id,

            Project.organization_id == organization_id

        ).first()





    def get_executions(

        self,

        db: Session,

        project_id: int,

        organization_id: int

    ):


        return db.query(

            ExecutionRecord

        ).join(

            Project

        ).filter(

            ExecutionRecord.project_id == project_id,

            Project.organization_id == organization_id

        ).order_by(

            ExecutionRecord.created_at.desc()

        ).all()