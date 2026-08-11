from app.agents.base_agent import BaseAgent

from app.shared.models.execution import ExecutionContext

from app.shared.models.artifact import Artifact



class ArchitectAgent(BaseAgent):

    """
    Responsible for designing
    system architecture and producing
    architecture artifacts.
    """


    name = "ArchitectAgent"

    role = "architect"



    def run(

        self,

        context: ExecutionContext

    ) -> dict:


        # =========================================
        # Collect Planner Tasks
        # =========================================

        tasks = [

            {

                "name": task.name,

                "status": task.status.value

            }

            for task in context.tasks

        ]



        # =========================================
        # Generate Architecture
        # =========================================

        architecture = {


            "backend": {

                "technology": "FastAPI",

                "architecture": "REST API"

            },


            "database": {

                "technology": "PostgreSQL",

                "orm": "SQLAlchemy"

            },


            "frontend": {

                "technology": "React",

                "type": "SPA"

            },


            "deployment": {

                "technology": "Docker",

                "environment": "Cloud"

            }

        }



        # =========================================
        # Create Artifact
        # =========================================

        artifact = Artifact(

            execution_id=context.id,

            created_by_agent=self.name,

            artifact_type="ARCHITECTURE",

            name="System Architecture Design",

            content=architecture

        )



        context.add_artifact(

            artifact

        )



        # =========================================
        # Save Result
        # =========================================

        result = {


            "agent": self.name,

            "role": self.role,

            "input_tasks": tasks,

            "architecture": architecture,

            "artifact": artifact.name

        }



        context.metadata[

            "architecture_result"

        ] = result



        return result