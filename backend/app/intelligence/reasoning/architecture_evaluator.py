class ArchitectureEvaluator:
    """
    Evaluates architecture candidates
    and calculates final decision score.
    """


    def evaluate(
        self,
        candidates: list,
        requirements: dict
    ) -> list:


        evaluated = []


        for candidate in candidates:


            architecture = candidate.get(
                "architecture",
                {}
            )


            scores = self.calculate_scores(
                architecture,
                requirements
            )


            final_score = (

                scores["development_speed"] * 0.25

                +

                scores["scalability"] * 0.30

                +

                scores["security"] * 0.20

                +

                scores["cost_efficiency"] * 0.25

            )


            evaluated.append(

                {

                    **candidate,

                    "scores": scores,

                    "final_score": round(
                        final_score,
                        2
                    )

                }

            )


        evaluated.sort(

            key=lambda item:
                item["final_score"],

            reverse=True

        )


        return evaluated



    # =============================================
    # Architecture Scoring
    # =============================================


    def calculate_scores(

        self,

        architecture: dict,

        requirements: dict

    ) -> dict:


        backend = architecture.get(
            "backend",
            {}
        )


        technology = backend.get(
            "technology"
        )


        scores = {

            "development_speed": 0.5,

            "scalability": 0.5,

            "security": 0.5,

            "cost_efficiency": 0.5

        }



        # Firebase

        if technology == "Firebase":


            scores["development_speed"] = 0.95

            scores["scalability"] = 0.75

            scores["security"] = 0.80

            scores["cost_efficiency"] = 0.90



        # FastAPI

        elif technology == "FastAPI":


            scores["development_speed"] = 0.70

            scores["scalability"] = 0.95

            scores["security"] = 0.90

            scores["cost_efficiency"] = 0.65



        # Node.js

        elif technology == "Node.js":


            scores["development_speed"] = 0.85

            scores["scalability"] = 0.80

            scores["security"] = 0.75

            scores["cost_efficiency"] = 0.75



        return scores