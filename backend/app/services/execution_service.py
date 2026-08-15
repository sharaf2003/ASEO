from sqlalchemy.orm import Session
from datetime import datetime


from app.repositories.execution_repository import (
    ExecutionRepository
)


from app.repositories.task_repository import (
    TaskRepository
)


from app.repositories.artifact_repository import (
    ArtifactRepository
)


from app.models.task import Task

from app.models.artifact import Artifact



class ExecutionService:

    """
    Execution management service.

    Handles ASEO execution lifecycle,
    tasks persistence and artifacts persistence.
    """



    # =====================================================
    # Allowed Execution Status Transitions
    # =====================================================

    ALLOWED_TRANSITIONS = {


        "PENDING": {

            "RUNNING",

            "FAILED",

        },


        "RUNNING": {

            "SUCCESS",

            "FAILED",

        },


        "SUCCESS": set(),


        "FAILED": set(),

    }



    def __init__(self):

        self.repository = ExecutionRepository()

        self.task_repository = TaskRepository()

        self.artifact_repository = ArtifactRepository()



    # =====================================================
    # Create Execution
    # =====================================================

    def create_execution(

        self,

        db: Session,

        project_id: int,

        organization_id: int,

        request: str,

        execution: dict

    ):


        if not project_id:

            raise ValueError(
                "Project ID is required"
            )



        if not organization_id:

            raise ValueError(
                "Organization ID is required"
            )



        if not request:

            raise ValueError(
                "Execution request is required"
            )


        try:


            execution_record = self.repository.create(

                db,

                project_id,

                request,

                execution.get(
                    "team",
                    {}
                ),

                execution.get(
                    "software",
                    {}
                ),

                execution.get(
                    "deployment",
                    {}
                ),

                execution.get(
                    "operations",
                    {}
                ),

                "PENDING"

            )



            db.commit()


            db.refresh(

                execution_record

            )


            return execution_record



        except Exception:


            db.rollback()

            raise



    # =====================================================
    # Validate Status Transition
    # =====================================================

    def _validate_transition(

        self,

        current_status: str,

        new_status: str

    ):


        current_status = str(

            current_status

        ).strip().upper()



        new_status = str(

            new_status

        ).strip().upper()



        allowed_statuses = (

            self.ALLOWED_TRANSITIONS.get(

                current_status

            )

        )



        if allowed_statuses is None:

            raise ValueError(

                f"Unknown execution status: {current_status}"

            )



        if new_status not in allowed_statuses:

            raise ValueError(

                f"Invalid execution status transition: "
                f"{current_status} -> {new_status}"

            )



    # =====================================================
    # Change Execution Status
    # =====================================================

    def _change_status(

        self,

        db: Session,

        execution_id: int,

        organization_id: int,

        new_status: str

    ):


        execution = self.repository.get_by_id(

            db,

            execution_id,

            organization_id

        )



        if not execution:

            raise ValueError(

                "Execution not found"

            )



        new_status = str(

            new_status

        ).strip().upper()



        self._validate_transition(

            execution.status,

            new_status

        )



        try:


            execution = self.repository.update_status(

                db,

                execution_id,

                organization_id,

                new_status

            )



            db.commit()


            db.refresh(

                execution

            )



            return execution



        except Exception:


            db.rollback()

            raise



    # =====================================================
    # Start Execution
    # =====================================================

    def start_execution(

        self,

        db: Session,

        execution_id: int,

        organization_id: int

    ):


        return self._change_status(

            db,

            execution_id,

            organization_id,

            "RUNNING"

        )



    # =====================================================
    # Complete Execution
    # =====================================================

    def complete_execution(

        self,

        db: Session,

        execution_id: int,

        organization_id: int

    ):


        return self._change_status(

            db,

            execution_id,

            organization_id,

            "SUCCESS"

        )



    # =====================================================
    # Fail Execution
    # =====================================================

    def fail_execution(

        self,

        db: Session,

        execution_id: int,

        organization_id: int

    ):


        return self._change_status(

            db,

            execution_id,

            organization_id,

            "FAILED"

        )



    # =====================================================
    # Create Task
    # =====================================================

    def create_task(

        self,

        db: Session,

        execution_id: int,

        name: str,

        description: str | None,

        agent_name: str,

        status: str = "PENDING",

        input_data: dict | None = None

    ):


        task = Task(

            execution_id=execution_id,

            name=name,

            description=description,

            agent_name=agent_name,

            status=status,

            input_data=input_data

        )


        return self.task_repository.create(

            db,

            task

        )



    # =====================================================
    # Update Task Status
    # =====================================================

    def update_task_status(

        self,

        db: Session,

        task: Task,

        status: str

    ):


        return self.task_repository.update_status(

            db,

            task,

            status

        )


    # =====================================================
    # Start Task
    # =====================================================

    def start_task(

        self,

        db: Session,

        task_id: int

    ):

        task = (

            db.query(Task)

            .filter(

                Task.id == task_id

            )

            .first()

        )


        if not task:

            raise ValueError(
                "Task not found"
            )


        task.status = "RUNNING"

        task.started_at = datetime.utcnow()


        db.commit()

        db.refresh(task)


        return task



    # =====================================================
    # Complete Task
    # =====================================================

    def complete_task(

        self,

        db: Session,

        task_id: int,

        output_data: dict | None = None

    ):


        task = (

            db.query(Task)

            .filter(

                Task.id == task_id

            )

            .first()

        )


        if not task:

            raise ValueError(
                "Task not found"
            )


        task.status = "COMPLETED"

        task.output_data = output_data

        task.completed_at = datetime.utcnow()


        db.commit()

        db.refresh(task)


        return task



    # =====================================================
    # Fail Task
    # =====================================================

    def fail_task(

        self,

        db: Session,

        task_id: int,

        error: Exception | str

    ):


        task = (

            db.query(Task)

            .filter(

                Task.id == task_id

            )

            .first()

        )


        if not task:

            raise ValueError(
                "Task not found"
            )


        task.status = "FAILED"

        task.output_data = {

            "error": str(error)

        }


        task.completed_at = datetime.utcnow()


        db.commit()

        db.refresh(task)


        return task



    # =====================================================
    # Create Artifact
    # =====================================================

    def create_artifact(

        self,

        db: Session,

        execution_id: int,

        created_by_agent: str,

        artifact_type: str,

        name: str,

        content: dict | None = None,

        extra_data: dict | None = None

    ):


        artifact = Artifact(

            execution_id=execution_id,

            created_by_agent=created_by_agent,

            artifact_type=artifact_type,

            name=name,

            content=content,

            extra_data=extra_data

        )


        return self.artifact_repository.create(

            db,

            artifact

        )



    # =====================================================
    # Get Execution
    # =====================================================

    def get_execution(

        self,

        db: Session,

        execution_id: int,

        organization_id: int

    ):


        execution = self.repository.get_by_id(

            db,

            execution_id,

            organization_id

        )



        if not execution:

            raise ValueError(

                "Execution not found"

            )



        return execution



    # =====================================================
    # Get Project Executions
    # =====================================================

    def get_project_executions(

        self,

        db: Session,

        project_id: int,

        organization_id: int

    ):


        return self.repository.get_by_project(

            db,

            project_id,

            organization_id

        )