from sqlalchemy.orm import Session

from app.models.execution_record import ExecutionRecord





class ExecutionRepository:



    def create(

        self,

        db: Session,

        project_id: int,

        request: str,

        team: dict | None = None,

        software: dict | None = None,

        deployment: dict | None = None,

        operations: dict | None = None,

        status: str = "QUEUED"

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





    def get_by_id(

        self,

        db: Session,

        execution_id: int

    ):


        return (

            db.query(ExecutionRecord)

            .filter(

                ExecutionRecord.id == execution_id

            )

            .first()

        )





    def get_by_project(

        self,

        db: Session,

        project_id: int

    ):


        return (

            db.query(ExecutionRecord)

            .filter(

                ExecutionRecord.project_id == project_id

            )

            .all()

        )





    def update_status(

        self,

        db: Session,

        execution_id: int,

        status: str

    ):


        execution = self.get_by_id(

            db,

            execution_id

        )


        if not execution:

            return None



        execution.status = status


        db.commit()

        db.refresh(execution)


        return execution