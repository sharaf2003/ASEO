from sqlalchemy.orm import Session

from app.repositories.execution_repository import (
    ExecutionRepository
)



class ExecutionService:

    """
    Execution management service.

    Handles ASEO execution lifecycle.
    """



    def __init__(self):

        self.repository = ExecutionRepository()



    # ==========================
    # Create Execution
    # ==========================


    def create_execution(

        self,

        db: Session,

        project_id: int,

        request: str,

        execution: dict

    ):


        return self.repository.create(

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



    # ==========================
    # Start Execution
    # ==========================


    def start_execution(

        self,

        db: Session,

        execution_id: int

    ):


        return self.repository.update_status(

            db,

            execution_id,

            "RUNNING"

        )



    # ==========================
    # Complete Execution
    # ==========================


    def complete_execution(

        self,

        db: Session,

        execution_id: int

    ):


        return self.repository.update_status(

            db,

            execution_id,

            "SUCCESS"

        )



    # ==========================
    # Fail Execution
    # ==========================


    def fail_execution(

        self,

        db: Session,

        execution_id: int

    ):


        return self.repository.update_status(

            db,

            execution_id,

            "FAILED"

        )



    # ==========================
    # Get Project Executions
    # ==========================


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