from .project_context import (
    ProjectContext
)

from .build_pipeline import (
    BuildPipeline
)



class SoftwareFactoryEngine:
    """
    ASEO Software Factory Engine v15

    First layer of autonomous
    software production.
    """



    def __init__(
        self
    ):


        self.pipeline = BuildPipeline()





    def create_project(
        self,
        requirement
    ):


        context = ProjectContext(

            requirement

        )



        self.pipeline.add_stage(

            "architecture"

        )


        self.pipeline.add_stage(

            "code_generation"

        )


        self.pipeline.add_stage(

            "testing"

        )



        stages = self.pipeline.execute()



        context.status = "factory_ready"



        return {


            "version":

                "15.0",


            "status":

                "factory_ready",


            "project":

                context.to_dict(),


            "pipeline":

                stages

        }