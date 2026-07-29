class PipelineManager:
    """
    ASEO Pipeline Manager v2.0

    Controls autonomous software engineering
    execution order.
    """



    def __init__(self):

        self.pipeline = [

            "document",

            "memory",

            "planning",

            "coding",

            "testing",

            "healing",

            "security",

            "quality",

            "optimization",

            "architecture",

            "database",

            "api",

            "senior_review",

            "deployment",

            "documentation",

            "delivery"

        ]





    def get_pipeline(
        self
    ):

        return self.pipeline





    def get_next_step(
        self,
        current_step
    ):


        if current_step not in self.pipeline:

            return None



        index = self.pipeline.index(

            current_step

        )



        if index + 1 >= len(self.pipeline):

            return None



        return self.pipeline[

            index + 1

        ]





    def contains(
        self,
        step
    ):

        return step in self.pipeline