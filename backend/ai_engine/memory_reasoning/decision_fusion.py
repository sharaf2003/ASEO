class DecisionFusion:
    """
    ASEO Decision Fusion Engine v14
    """



    def combine(
        self,
        decision,
        memories
    ):


        if not memories:

            decision["based_on_memory"] = False

            return decision



        best_memory = memories[0]



        decision["previous_solution"] = (

            best_memory.get(

                "decision",

                best_memory.get(
                    "technology",
                    ""
                )

            )

        )


        decision["based_on_memory"] = True


        decision["confidence"] = min(

            decision.get(

                "confidence",

                0.8

            )
            +
            0.1,

            1.0

        )


        return decision