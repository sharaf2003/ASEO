from sqlalchemy.orm import Session

from app.models.execution_record import ExecutionRecord

from app.models.project import Project





class ExecutionRepository:
    """
    Repository for execution history.
    """



    # ==========================
    # Create Execution Record
    # ==========================


    def create(

        self,

        db: Session,

        project_id: int,

        request: str,

        team: dict,

        software: dict,

        deployment: dict,

        operations: dict,

        status: str = "completed"

    ):


        execution = ExecutionRecord(

            project_id=project_id,

            request=request,

            team=team,

            software=software,

            deployment=deployment,

            operations=operations,

            status=status

        )


        db.add(execution)

        db.commit()

        db.refresh(execution)


        return execution





    # ==========================
    # Get Project Executions
    # ==========================


    def get_by_project(

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