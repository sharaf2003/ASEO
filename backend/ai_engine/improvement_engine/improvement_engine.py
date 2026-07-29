from .experience import (
    Experience
)

from .improver import (
    Improver
)



class ContinuousImprovementEngine:
    """
    ASEO Continuous Improvement Engine v16
    """



    def __init__(
        self
    ):

        self.memory = []

        self.improver = Improver()





    def learn(
        self,
        problem,
        solution
    ):


        experience = Experience(

            problem,

            solution,

            True

        )



        data = experience.to_dict()



        self.memory.append(

            data

        )



        improvement = self.improver.improve(

            data

        )



        return {

            "experience":

                data,


            "improvement":

                improvement,


            "knowledge_updated":

                True

        }