class ExperienceRanker:
    """
    ASEO Experience Ranker v20.2
    """

    def rank(
        self,
        experiences
    ):


        return sorted(

            experiences,

            key=lambda x:

            x.get(
                "result",
                {}
            ).get(
                "quality",
                0
            ),

            reverse=True

        )