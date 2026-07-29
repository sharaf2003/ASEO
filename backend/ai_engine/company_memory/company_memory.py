from .experience import (
    CompanyExperience
)


from .memory_store import (
    CompanyMemoryStore
)





class CompanyMemoryEngine:
    """
    ASEO Company Memory Engine v19.1

    Learns from completed projects.
    """



    def __init__(
        self
    ):


        self.store = CompanyMemoryStore()






    def remember(
        self,
        project,
        decision,
        result
    ):


        experience = CompanyExperience(

            project,

            decision,

            result

        )



        self.store.save(

            experience.to_dict()

        )



        return experience.to_dict()





    def recall(
        self,
        keyword
    ):


        results = []



        for memory in self.store.all():


            if keyword.lower() in memory["project"].lower():

                results.append(

                    memory

                )



        return results