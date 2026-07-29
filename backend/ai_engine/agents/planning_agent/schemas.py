class ProjectPlanSchema:
    """
    ASEO Project Plan Schema v2
    """



    def __init__(
        self,
        phases
    ):

        self.phases = phases




    def to_dict(
        self
    ):


        return {


            "project_phases":

                self.phases


        }