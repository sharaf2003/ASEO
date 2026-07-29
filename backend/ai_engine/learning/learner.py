from .experience import Experience




class LearningEngine:
    """
    ASEO Learning Engine v14

    Learns from completed projects.
    """



    def __init__(self):

        self.experiences = []





    def learn(
        self,
        project,
        decision,
        result,
        success=True,
        score=100
    ):


        experience = Experience(

            project,

            decision,

            result,

            success,

            score

        )


        self.experiences.append(

            experience

        )


        return experience.to_dict()





    def history(self):


        return [

            item.to_dict()

            for item

            in self.experiences

        ]