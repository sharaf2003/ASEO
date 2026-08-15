from sqlalchemy.orm import Session


from ai_engine.company_platform.company_orchestrator import (
    CompanyOrchestrator
)


from ai_engine.autonomous_company.execution_pipeline import (
    ExecutionPipeline
)


from app.agents.orchestrator import (
    AgentOrchestrator
)


from app.models.project import Project


from app.services.execution_service import (
    ExecutionService
)


from app.services.lifecycle_service import (
    LifecycleService
)



class ASEOEngineService:

    """
    ASEO Production Engine.

    Responsible for coordinating:

    - Agent Orchestration
    - Execution Lifecycle
    - Project Lifecycle
    - Company Analysis
    - Legacy Execution Pipeline
    """


    def __init__(self):

        self.company = CompanyOrchestrator()

        self.pipeline = ExecutionPipeline()

        self.execution_service = ExecutionService()

        self.lifecycle = LifecycleService()



    # =====================================================
    # Execute Project
    # =====================================================

    def execute_project(

        self,

        db: Session,

        project_name: str,

        organization_id: int

    ):


        project_name = project_name.strip()



        if not project_name:

            raise ValueError(
                "Project name is required"
            )



        # =================================================
        # Load Project With Tenant Isolation
        # =================================================

        project = (

            db.query(Project)

            .filter(

                Project.name == project_name,

                Project.organization_id == organization_id

            )

            .first()

        )



        if not project:

            raise ValueError(
                "Project not found"
            )



        execution_record = None



        try:


            # =============================================
            # Create Execution Record
            # =============================================

            execution_record = (

                self.execution_service.create_execution(

                    db,

                    project.id,

                    organization_id,

                    project.name,

                    {}

                )

            )

            # =============================================
            # Start Execution
            # =============================================

            self.execution_service.start_execution(

                db,

                execution_record.id,

                organization_id

            )


            # =============================================
            # Initialize Agent Orchestrator
            # =============================================

            agent_orchestrator = AgentOrchestrator(

                    db=db,

                    project_id=project.id,

                    organization_id=organization_id
            )



            # =============================================
            # Project Lifecycle
            # =============================================

            if project.status in [
                "created",
                "operational"
            ]:

                self.lifecycle.update_status(

                    db,

                    project,

                    "analyzing"

                )


            # =============================================
            # Agent Execution
            # =============================================

            agents_result = (

                agent_orchestrator.run(

                    request=project.name,

                    project_id=project.id,

                    organization_id=organization_id,

                    execution_id=execution_record.id

                )

            )

            # =============================================
            # Persist Agent Tasks
            # =============================================

            for task in agents_result.get(
                "tasks",
                []
            ):

                db_task = self.execution_service.create_task(

                    db,

                    execution_record.id,

                    task.get(
                        "name",
                        "Unnamed Task"
                    ),

                    task.get(
                        "description"
                    ),

                    task.get(
                        "agent",
                        "Unknown Agent"
                    ),

                    "PENDING",
                    

                    task

                )

                self.execution_service.start_task(

                    db,

                    db_task.id

                )

                self.execution_service.complete_task(

                    db,

                    db_task.id,

                    task

                )


            # =============================================
            # Persist Agent Artifacts
            # =============================================

            for artifact in agents_result.get(
                "artifacts",
                []
            ):


                self.execution_service.create_artifact(

                    db,

                    execution_record.id,

                    artifact.get(

                        "agent",

                        "Unknown Agent"
                            
                    ),

                    artifact.get(

                        "type",

                        "DOCUMENT"

                    ),

                    artifact.get(

                        "name",

                        "Unnamed Artifact"

                    ),

                    artifact,

                    {}

                )



            # =============================================
            # Company Analysis
            # =============================================

            analysis = (

                self.company.run(

                    project.name

                )

            )


            # =============================================
            # Building Phase
            # =============================================

            if project.status == "analyzing":

                self.lifecycle.update_status(

                    db,

                    project,

                    "building"

                )



            # =============================================
            # Legacy Pipeline Support
            # =============================================

            execution = (

                self.pipeline.execute(

                    project.name

                )

            )



            # =============================================
            # Save Agent Results
            # =============================================

            execution_record.team = {


                "tasks": (

                    agents_result.get(

                        "tasks",

                        []

                    )

                )

            }



            execution_record.software = {


                "artifacts": (

                    agents_result.get(

                        "artifacts",

                        []

                    )

                )

            }

            execution_record.operations = {

                "metadata": (

                    agents_result.get(

                        "metadata",

                        {}

                    )

                )

            }

            execution_record.deployment = (

                execution.get(

                    "deployment",

                    {}

                )

            )

            db.commit()

            # =============================================
            # Deployment Lifecycle
            # =============================================

            if project.status == "building":

                self.lifecycle.update_status(

                    db,

                    project,

                    "deploying"

                )

            # =============================================
            # Complete Execution
            # =============================================

            self.execution_service.complete_execution(

                db,

                execution_record.id,

                organization_id

            )

            # =============================================
            # Operational Lifecycle
            # =============================================

            if project.status == "deploying":

                self.lifecycle.update_status(

                    db,

                    project,

                    "operational"

                )

            # =============================================
            # Final Response
            # =============================================

            return {


                "project": project.name,


                "project_id": project.id,


                "organization_id": project.organization_id,


                "lifecycle_status": project.status,


                "agents": agents_result,


                "analysis": analysis,


                "execution": execution,


                "execution_record_id": execution_record.id,


                "status": "SUCCESS"

            }



        except Exception :


            db.rollback()



            if execution_record:


                self.execution_service.fail_execution(

                    db,

                    execution_record.id,

                    organization_id

                )


            raise 