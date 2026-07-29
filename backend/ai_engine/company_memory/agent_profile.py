from datetime import datetime
from uuid import uuid4



class AgentProfile:
    """
    ASEO Agent Profile v19.2

    Stores agent performance.
    """



    def __init__(
        self,
        agent_name,
        role
    ):


        self.id = str(uuid4())

        self.agent_name = agent_name

        self.role = role

        self.tasks_completed = 0

        self.tasks_failed = 0

        self.quality_scores = []

        self.created_at = datetime.now()





    def update(
        self,
        success,
        quality
    ):


        if success:

            self.tasks_completed += 1

        else:

            self.tasks_failed += 1



        self.quality_scores.append(

            quality

        )







    def success_rate(
        self
    ):


        total = (

            self.tasks_completed

            +

            self.tasks_failed

        )


        if total == 0:

            return 0



        return (

            self.tasks_completed

            /

            total

        ) * 100






    def average_quality(
        self
    ):


        if not self.quality_scores:

            return 0



        return sum(

            self.quality_scores

        ) / len(self.quality_scores)






    def to_dict(
        self
    ):


        return {


            "id":

                self.id,


            "agent":

                self.agent_name,


            "role":

                self.role,


            "tasks_completed":

                self.tasks_completed,


            "tasks_failed":

                self.tasks_failed,


            "success_rate":

                self.success_rate(),


            "quality_score":

                self.average_quality()


        }