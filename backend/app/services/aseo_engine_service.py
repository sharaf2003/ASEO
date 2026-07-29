from sqlalchemy.orm import Session


from ai_engine.company_platform.company_orchestrator import (
    CompanyOrchestrator
)


from ai_engine.autonomous_company.execution_pipeline import (
    ExecutionPipeline
)


from app.models.project import (
    Project
)


from app.services.execution_service import (
    ExecutionService
)


from app.services.lifecycle_service import (
    LifecycleService
)





class ASEOEngineService:
    """
    ASEO Production Engine v22.9

    Autonomous execution
    with:

    - Executive Analysis
    - AI Pipeline Execution
    - Execution History
    - Project Lifecycle Management
    """



    def __init__(self):

        self.company = CompanyOrchestrator()

        self.pipeline = ExecutionPipeline()

        self.execution_service = ExecutionService()

        self.lifecycle = LifecycleService()





    def execute_project(
        self,
        db: Session,
        project_name
    ):



        # ==========================
        # Find Project
        # ==========================


        project = db.query(Project).filter(

            Project.name == project_name

        ).first()



        if not project:

            raise Exception(
                "Project not found"
            )





        # ==========================
        # Lifecycle: Analysis
        # ==========================


        self.lifecycle.update_status(

            db,

            project,

            "analyzing"

        )





        # ==========================
        # Executive Analysis
        # ==========================


        analysis = self.company.run(

            project_name

        )





        # ==========================
        # Lifecycle: Building
        # ==========================


        self.lifecycle.update_status(

            db,

            project,

            "building"

        )





        # ==========================
        # Autonomous Execution
        # ==========================


        execution = self.pipeline.execute(

            project_name

        )





        # ==========================
        # Lifecycle: Deploying
        # ==========================


        self.lifecycle.update_status(

            db,

            project,

            "deploying"

        )





        # ==========================
        # Save Execution History
        # ==========================


        record = self.execution_service.create_execution(

            db,

            project.id,

            project_name,

            execution

        )





        # ==========================
        # Lifecycle: Operational
        # ==========================


        self.lifecycle.update_status(

            db,

            project,

            "operational"

        )





        # ==========================
        # Response
        # ==========================


        return {


            "project":

                project_name,


            "project_id":

                project.id,


            "lifecycle_status":

                project.status,


            "analysis":

                analysis,


            "execution":

                execution,


            "execution_record_id":

                record.id,


            "status":

                "completed"

        }