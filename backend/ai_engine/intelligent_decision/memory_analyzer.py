class MemoryAnalyzer:
    """
    ASEO Memory Analyzer v20.2
    """

    def analyze(
        self,
        memories,
        requirement
    ):

        matches = []


        keyword = requirement.lower().split()[1]


        for memory in memories:

            project = memory.get(
                "project",
                ""
            ).lower()


            if keyword in project:

                matches.append(memory)



        return matches