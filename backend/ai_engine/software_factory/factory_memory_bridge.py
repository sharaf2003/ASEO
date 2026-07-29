from ai_engine.company_memory.memory_adapter import (
    MemoryAdapter
)



class FactoryMemoryBridge:
    """
    ASEO Software Factory Memory Bridge v21.3
    """

    def __init__(self):

        self.memory = MemoryAdapter()



    def save_result(
        self,
        project,
        result
    ):

        return self.memory.save_decision(

            project,

            "Software Factory Execution",

            result

        )