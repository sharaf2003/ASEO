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

        organization_id: int

    ):


        project_name = project_name.strip()


        if not project_name:

            raise ValueError(
                "Project name is required"
            )



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


            # =========================================
            # Create Execution
            # =========================================

            execution_record = (

                self.execution_service.create_execution(

                    db,

                    project.id,

                    organization_id,

                    project.name,

                    {}

                )

            )



            # =========================================
            # Start Execution
            # =========================================

            self.execution_service.start_execution(

                db,

                execution_record.id,

                organization_id

            )



            self.lifecycle.update_status(

                db,

                project,

                "analyzing"

            )



            # =========================================
            # Agents
            # =========================================

            agents_result = (

                self.agent_orchestrator.run(

                    project.name

                )

            )



            # =========================================
            # Company Analysis
            # =========================================

            analysis = (

                self.company.run(

                    project.name

                )

            )



            self.lifecycle.update_status(

                db,

                project,

                "building"

            )



            # =========================================
            # Pipeline
            # =========================================

            execution = (

                self.pipeline.execute(

                    project.name

                )

            )



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



            self.lifecycle.update_status(

                db,

                project,

                "deploying"

            )



            self.execution_service.complete_execution(

                db,

                execution_record.id,

                organization_id

            )



            self.lifecycle.update_status(

                db,

                project,

                "operational"

            )



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


            db.rollback()



            if execution_record:


                self.execution_service.fail_execution(

                    db,

                    execution_record.id,

                    organization_id

                )


            raise