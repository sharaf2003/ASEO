class DecisionReasoner:
    """
    ASEO Decision Reasoning v16.7
    """



    def explain(
        self,
        decision
    ):


        return (

            f"Selected {decision['framework']} "
            f"with {decision['database']} "
            "based on previous engineering knowledge"

        )