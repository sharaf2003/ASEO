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



    def execute_project(

        self,

        db: Session,

        project_name: str

    ):


        project = (

            db.query(Project)

            .filter(

                Project.name == project_name

            )

            .first()

        )


        if not project:

            raise Exception(
                "Project not found"
            )



        execution_record = None



        try:


            # ==========================
            # Create Execution
            # ==========================


            execution_record = (

                self.execution_service.create_execution(

                    db,

                    project.id,

                    project_name,

                    {}

                )

            )



            # ==========================
            # Start Execution
            # ==========================


            self.execution_service.start_execution(

                db,

                execution_record.id

            )



            self.lifecycle.update_status(

                db,

                project,

                "analyzing"

            )



            # ==========================
            # Agent Orchestration
            # ==========================


            agents_result = self.agent_orchestrator.run(

                project_name

            )



            # ==========================
            # Executive Analysis
            # ==========================


            analysis = self.company.run(

                project_name

            )



            self.lifecycle.update_status(

                db,

                project,

                "building"

            )



            # ==========================
            # Pipeline Execution
            # ==========================


            execution = self.pipeline.execute(

                project_name

            )



            # ==========================
            # Save Execution Data
            # ==========================


            execution_record.team = {


                "plan":

                    agents_result.get(

                        "plan",

                        {}

                    )

            }



            execution_record.software = {


                "architecture":

                    agents_result.get(

                        "architecture",

                        {}

                    )

            }



            execution_record.operations = {


                "development":

                    agents_result.get(

                        "development",

                        {}

                    )

            }



            execution_record.deployment = execution.get(

                "deployment",

                {}

            )



            db.commit()



            self.lifecycle.update_status(

                db,

                project,

                "deploying"

            )



            self.execution_service.complete_execution(

                db,

                execution_record.id

            )



            self.lifecycle.update_status(

                db,

                project,

                "operational"

            )



            return {


                "project":

                    project_name,


                "project_id":

                    project.id,


                "lifecycle_status":

                    project.status,


                "agents":

                    agents_result,


                "analysis":

                    analysis,


                "execution":

                    execution,


                "execution_record_id":

                    execution_record.id,


                "status":

                    "SUCCESS"

            }



        except Exception as error:


            if execution_record:


                self.execution_service.fail_execution(

                    db,

                    execution_record.id

                )


            raise error