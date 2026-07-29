class PerformanceAnalyzer:
    """
    ASEO Performance Analyzer v20.4
    """

    def analyze(
        self,
        agents
    ):

        best_agent = None

        best_score = 0


        for agent in agents:

            score = agent.get(
                "quality_score",
                0
            )


            if score > best_score:

                best_score = score

                best_agent = agent["agent"]



        return {

            "best_agent":
                best_agent,

            "best_score":
                best_score,

            "analysis":
                "Selected highest performing agent"

        }