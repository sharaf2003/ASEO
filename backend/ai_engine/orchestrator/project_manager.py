import uuid
from datetime import datetime





class ProjectManager:
    """
    ASEO Project Manager v2.0

    Handles project lifecycle
    and metadata management.
    """



    def create_project(
        self,
        name="ASEO Project"
    ):


        return {


            "project_id":

                str(uuid.uuid4()),



            "name":

                name,



            "created_at":

                datetime.now().isoformat(),



            "status":

                "initialized",



            "agents":

                [],



            "metadata":

                {

                    "version":

                        "12.0"

                }

        }





    def update_status(
        self,
        project,
        status
    ):


        project["status"] = status


        project["updated_at"] = (

            datetime.now().isoformat()

        )


        return project





    def register_agent(
        self,
        project,
        agent_name
    ):


        if agent_name not in project["agents"]:

            project["agents"].append(

                agent_name

            )


        return project