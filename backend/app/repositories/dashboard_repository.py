from sqlalchemy.orm import Session

from app.models.project import Project

from app.models.execution_record import ExecutionRecord





class DashboardRepository:
    """
    Repository for project dashboard data.
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