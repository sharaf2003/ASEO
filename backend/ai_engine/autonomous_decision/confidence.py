class ConfidenceCalculator:
    """
    ASEO Decision Confidence v16.7
    """



    def calculate(
        self,
        sources
    ):


        score = 0


        if "memory" in sources:

            score += 0.3



        if "agents" in sources:

            score += 0.3



        if "brain" in sources:

            score += 0.3



        if "improvement" in sources:

            score += 0.1



        return min(
            score,
            1.0
        )