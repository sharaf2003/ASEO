class DecisionAnalyzer:
    """
    ASEO Knowledge Decision Analyzer v14
    """



    def analyze(
        self,
        memories
    ):


        recommendations = {}


        for memory in memories:


            if "decision" in memory:


                decision = memory["decision"]


                if "FastAPI" in decision:

                    recommendations["framework"] = "FastAPI"


                if "PostgreSQL" in decision:

                    recommendations["database"] = "PostgreSQL"



            if "technology" in memory:


                technology = memory["technology"]


                if "FastAPI" in technology:

                    recommendations["framework"] = "FastAPI"


                if "PostgreSQL" in technology:

                    recommendations["database"] = "PostgreSQL"



        return recommendations