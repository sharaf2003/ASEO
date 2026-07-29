from .company_memory import CompanyMemoryEngine



class MemoryAdapter:
    """
    ASEO Memory Adapter v21.1

    Connects Company Memory
    with Autonomous Company Platform.
    """

    def __init__(self):

        self.memory = CompanyMemoryEngine()



    def save_decision(
        self,
        project,
        decision,
        result
    ):


        return self.memory.remember(

            project,

            decision,

            result

        )



    def recall_history(
        self,
        project
    ):


        return self.memory.recall(

            project

        )