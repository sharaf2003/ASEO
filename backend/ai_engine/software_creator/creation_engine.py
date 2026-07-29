from .creator import (
    SoftwareCreator
)



class AutonomousSoftwareCreationEngine:
    """
    ASEO Autonomous Software Creation Engine v17.1
    """



    def __init__(
        self
    ):


        self.creator = SoftwareCreator()





    def create(
        self,
        decision
    ):


        blueprint = self.creator.create_blueprint(

            decision

        )


        return {


            "version":

                "17.1",



            "status":

                "blueprint_created",



            "blueprint":

                blueprint

        }