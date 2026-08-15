class TradeoffAnalyzer:
    """
    Analyzes architecture trade-offs
    and explains the final decision.
    """


    def analyze(

        self,

        evaluated_architectures: list,

        requirements: dict

    ) -> dict:


        if not evaluated_architectures:

            return {}


        winner = evaluated_architectures[0]


        alternatives = evaluated_architectures[1:]


        analysis = {

            "recommended_architecture":
                winner.get(
                    "name"
                ),


            "score":
                winner.get(
                    "final_score"
                ),


            "reasoning": [],


            "advantages": [],


            "limitations": [],


            "alternatives": []

        }


        architecture = winner.get(
            "architecture",
            {}
        )


        backend = architecture.get(
            "backend",
            {}
        )


        technology = backend.get(
            "technology"
        )


        # =============================================
        # Firebase Reasoning
        # =============================================

        if technology == "Firebase":


            analysis["reasoning"].extend(

                [

                    "Project requires fast development",

                    "Mobile application benefits from managed backend",

                    "Low operational complexity is preferred"

                ]

            )


            analysis["advantages"].extend(

                [

                    "Fast MVP development",

                    "Low server maintenance",

                    "Built-in cloud services"

                ]

            )


            analysis["limitations"].extend(

                [

                    "Less backend customization",

                    "Vendor dependency"

                ]

            )



        # =============================================
        # FastAPI Reasoning
        # =============================================

        elif technology == "FastAPI":


            analysis["reasoning"].extend(

                [

                    "Project requires high control",

                    "Backend customization is important"

                ]

            )


            analysis["advantages"].extend(

                [

                    "High scalability",

                    "Full backend control",

                    "Flexible architecture"

                ]

            )


            analysis["limitations"].extend(

                [

                    "Higher maintenance",

                    "More development effort"

                ]

            )



        # =============================================
        # Alternatives
        # =============================================

        for alternative in alternatives:


            analysis["alternatives"].append(

                {

                    "name":
                        alternative.get(
                            "name"
                        ),


                    "score":
                        alternative.get(
                            "final_score"
                        ),


                    "reason":

                        "Suitable alternative with different trade-offs"

                }

            )


        return analysis