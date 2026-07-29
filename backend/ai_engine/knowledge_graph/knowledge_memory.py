class KnowledgeMemory:
    """
    ASEO Knowledge Memory v21.6
    """

    def __init__(self):

        self.memory = []



    def store(
        self,
        knowledge
    ):

        self.memory.append(

            knowledge

        )

        return knowledge



    def recall(
        self,
        keyword
    ):

        results = []


        for item in self.memory:

            if keyword.lower() in str(item).lower():

                results.append(item)


        return results



    def all(self):

        return self.memory