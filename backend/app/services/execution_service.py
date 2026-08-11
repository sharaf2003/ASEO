from sqlalchemy.orm import Session

from app.repositories.execution_repository import (
    ExecutionRepository
)


class ExecutionService:

    """
    Execution management service.

    Handles ASEO execution lifecycle.
    """


    # =====================================================
    # Allowed Execution Status Transitions
    # =====================================================

    ALLOWED_TRANSITIONS = {

        "QUEUED": {
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

                "QUEUED"

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