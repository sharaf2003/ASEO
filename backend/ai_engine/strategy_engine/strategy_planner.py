class StrategyPlanner:
    """
    ASEO Strategy Planner v21.8
    """

    def plan(
        self,
        idea,
        roi,
        risk
    ):


        decision = (

            "Build"

            if roi["roi"] > 100

            else

            "Review"

        )


        return {

            "idea":
                idea,

            "decision":
                decision,

            "priority":
                "high",

            "reason":
                "Strong ROI opportunity"

        }