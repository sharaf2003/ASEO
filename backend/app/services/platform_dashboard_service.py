from sqlalchemy.orm import Session


from app.repositories.project_repository import (
    ProjectRepository
)


from app.repositories.execution_repository import (
    ExecutionRepository
)


from app.repositories.api_key_repository import (
    APIKeyRepository
)


from app.repositories.api_usage_repository import (
    APIUsageRepository
)


from ai_engine.registry.agent_registry import (
    AgentRegistry
)





class PlatformDashboardService:

    """
    ASEO Platform Dashboard Service

    Provides global system overview:

    - Projects
    - Executions
    - Agents
    - API Usage
    """



    def __init__(self):

        self.project_repository = ProjectRepository()

        self.execution_repository = ExecutionRepository()

        self.api_key_repository = APIKeyRepository()

        self.api_usage_repository = APIUsageRepository()

        self.agent_registry = AgentRegistry()





    def get_overview(

        self,

        db: Session,

        organization_id: int

    ):


        # =========================
        # Projects
        # =========================


        projects = self.project_repository.get_all(

            db,

            organization_id

        )





        # =========================
        # Executions
        # =========================


        executions = self.execution_repository.get_all_by_organization(

            db,

            organization_id

        )





        # =========================
        # Agents
        # =========================


        agents = self.agent_registry.list_agents()





        # =========================
        # API Usage
        # =========================


        api_keys = self.api_key_repository.get_by_organization(

            db,

            organization_id

        )


        total_requests = 0


        for key in api_keys:

            total_requests += (

                self.api_usage_repository.get_request_count(

                    db,

                    key.id

                )

            )



        active_api_keys = len(

            [

                key

                for key in api_keys

                if key.status == "active"

            ]

        )





        # =========================
        # Statistics
        # =========================


        running_executions = len(

            [

                execution

                for execution in executions

                if execution.status == "RUNNING"

            ]

        )



        completed_executions = len(

            [

                execution

                for execution in executions

                if execution.status == "SUCCESS"

            ]

        )



        failed_executions = len(

            [

                execution

                for execution in executions

                if execution.status == "FAILED"

            ]

        )





        return {


            "system": {


                "name":

                    "ASEO Autonomous Engineering",


                "status":

                    "healthy"

            },



            "projects": {


                "total":

                    len(projects),


                "active":

                    len(

                        [

                            project

                            for project in projects

                            if project.status == "active"

                        ]

                    )

            },



            "executions": {


                "total":

                    len(executions),


                "running":

                    running_executions,


                "completed":

                    completed_executions,


                "failed":

                    failed_executions

            },



            "agents": {


                "total":

                    len(agents)

            },



            "api_usage": {


                "total_keys":

                    len(api_keys),


                "active_keys":

                    active_api_keys,


                "total_requests":

                    total_requests

            }

        }