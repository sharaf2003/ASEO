from sqlalchemy.orm import Session


from app.repositories.execution_repository import (
    ExecutionRepository
)




class ExecutionService:

    """
    Execution management service.

    Handles project execution history.
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

            "completed"

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