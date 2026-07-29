class CompanyMemoryStore:
    """
    ASEO Company Memory Storage v19.1
    """



    def __init__(
        self
    ):

        self.memories = []





    def save(
        self,
        experience
    ):


        self.memories.append(

            experience

        )


        return experience






    def all(
        self
    ):


        return self.memories