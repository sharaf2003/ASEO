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
    ASEO Production Engine v25.0

    Autonomous execution engine with:

    - Agent Orchestration
    - Planner Agent
    - Architect Agent
    - Developer Agent
    - Executive Analysis
    - AI Pipeline Execution
    - Execution Lifecycle
    - Execution History
    - Project Lifecycle Management
    """


    def __init__(self):

        self.company = CompanyOrchestrator()

        self.pipeline = ExecutionPipeline()

        self.agent_orchestrator = AgentOrchestrator()

        self.execution_service = ExecutionService()

        self.lifecycle = LifecycleService()


    # =================================================
    # Execute Project
    # =================================================

    def execute_project(
        self,
        db: Session,
        project_name: str,
        organization_id: int,
    ):

        # ---------------------------------------------
        # Normalize input
        # ---------------------------------------------

        project_name = project_name.strip()

        if not project_name:
            raise ValueError(
                "Project name is required"
            )


        # ---------------------------------------------
        # Tenant-safe project lookup
        # ---------------------------------------------

        project = (
            db.query(Project)
            .filter(
                Project.name == project_name,
                Project.organization_id == organization_id,
            )
            .first()
        )


        if not project:
            raise ValueError(
                "Project not found"
            )


        execution_record = None


        try:

            # =========================================
            # Create Execution
            # =========================================

            execution_record = (
                self.execution_service.create_execution(
                    db,
                    project.id,
                    project.name,
                    {}
                )
            )


            # =========================================
            # Start Execution
            # =========================================

            self.execution_service.start_execution(
                db,
                execution_record.id
            )


            # =========================================
            # Project Lifecycle: Analyzing
            # =========================================

            self.lifecycle.update_status(
                db,
                project,
                "analyzing"
            )


            # =========================================
            # Agent Orchestration
            # =========================================

            agents_result = (
                self.agent_orchestrator.run(
                    project.name
                )
            )


            # =========================================
            # Executive Analysis
            # =========================================

            analysis = self.company.run(
                project.name
            )


            # =========================================
            # Project Lifecycle: Building
            # =========================================

            self.lifecycle.update_status(
                db,
                project,
                "building"
            )


            # =========================================
            # Pipeline Execution
            # =========================================

            execution = self.pipeline.execute(
                project.name
            )


            # =========================================
            # Save Execution Data
            # =========================================

            execution_record.team = {
                "plan": agents_result.get(
                    "plan",
                    {}
                )
            }


            execution_record.software = {
                "architecture": agents_result.get(
                    "architecture",
                    {}
                )
            }


            execution_record.operations = {
                "development": agents_result.get(
                    "development",
                    {}
                )
            }


            execution_record.deployment = (
                execution.get(
                    "deployment",
                    {}
                )
            )


            db.commit()


            # =========================================
            # Project Lifecycle: Deploying
            # =========================================

            self.lifecycle.update_status(
                db,
                project,
                "deploying"
            )


            # =========================================
            # Complete Execution
            # =========================================

            self.execution_service.complete_execution(
                db,
                execution_record.id
            )


            # =========================================
            # Project Lifecycle: Operational
            # =========================================

            self.lifecycle.update_status(
                db,
                project,
                "operational"
            )


            # =========================================
            # Response
            # =========================================

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


        except Exception:

            # -----------------------------------------
            # Rollback failed database work
            # -----------------------------------------

            db.rollback()


            # -----------------------------------------
            # Mark execution as failed
            # -----------------------------------------

            if execution_record:

                self.execution_service.fail_execution(
                    db,
                    execution_record.id
                )


            raise