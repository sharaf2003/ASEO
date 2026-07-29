from .memory import (
    EngineeringMemory
)


from .experience_store import (
    ExperienceStore
)


from .retrieval import (
    MemoryRetriever
)





class EngineeringMemoryEngine:
    """
    ASEO Engineering Memory Engine v16.8.2

    Persistent Engineering Knowledge Base
    """



    def __init__(
        self
    ):


        self.store = ExperienceStore()


        self.retriever = MemoryRetriever()








    def remember(
        self,
        project,
        decision,
        result
    ):


        memory = EngineeringMemory(

            project,

            decision,

            result

        ).to_dict()





        self.store.save(

            memory

        )





        return memory







    def recall(
        self,
        keyword
    ):


        return self.retriever.search(

            self.store.all(),

            keyword

        )






    def get_all_memory(
        self
    ):


        return self.store.all()