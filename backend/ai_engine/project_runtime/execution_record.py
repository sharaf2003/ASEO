from datetime import datetime
import uuid



class ExecutionRecord:
    """
    ASEO Execution Record v22.9.2
    """

    def create(
        self,
        project,
        result
    ):

        return {

            "id":
                str(uuid.uuid4()),


            "project":
                project,


            "status":
                result.get(
                    "status",
                    "completed"
                ),


            "team":

                [
                    agent["agent"]

                    for agent in result
                    .get("team", {})
                    .get("agents", [])
                ],


            "deployment":

                result
                .get("deployment", {})
                .get(
                    "status",
                    "unknown"
                ),


            "created_at":

                datetime.now().isoformat()

        }