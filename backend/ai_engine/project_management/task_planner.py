from uuid import uuid4



class TaskPlanner:
    """
    ASEO Task Planner v22.0
    """

    def create_tasks(
        self,
        features
    ):

        tasks = []


        for feature in features:

            tasks.append(

                {

                    "id":
                        str(uuid4()),

                    "feature":
                        feature,

                    "status":
                        "planned"

                }

            )


        return tasks