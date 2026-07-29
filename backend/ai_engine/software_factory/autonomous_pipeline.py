from .factory_integration import SoftwareFactory

from .factory_memory_bridge import FactoryMemoryBridge




class AutonomousSoftwarePipeline:
    """
    ASEO Autonomous Software Factory v21.3

    Architecture
    +
    Generation
    +
    Testing
    +
    Memory
    """



    def __init__(self):

        self.factory = SoftwareFactory()

        self.memory = FactoryMemoryBridge()



    def build(
        self,
        requirement
    ):


        software = self.factory.create_software(

            requirement

        )


        memory = self.memory.save_result(

            requirement,

            software

        )


        return {

            "software":

                software,


            "memory":

                memory,


            "status":

                "factory_completed"

        }