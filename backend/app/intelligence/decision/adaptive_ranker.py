class AdaptiveDecisionRanker:


    """
    Ranks architecture decisions
    based on learned experience and project context.
    """



    def rank(

        self,

        patterns: list,

        context: dict = None

    ) -> list:


        ranked = []


        context = context or {}

        project_type = context.get(
            "project_type",
            ""
        )



        for pattern in patterns:


            success_rate = (

                pattern.get(
                    "success_rate",
                    0
                )

                /

                100

            )



            priority_score = pattern.get(

                "priority_score",

                0.5

            )



            confidence = pattern.get(

                "confidence",

                0.5

            )



            memory_score = pattern.get(

                "memory_score",

                0.5

            )



            adaptive_decision_score = pattern.get(

                "adaptive_decision_score",

                0.5

            )



            recency = pattern.get(

                "recency",

                0.5

            )



            failure_penalty = pattern.get(

                "failure_penalty",

                0

            )



            # ==============================
            # Context Matching
            # ==============================

            context_match = 0


            pattern_category = pattern.get(
                "category",
                ""
            )


            pattern_name = pattern.get(
                "name",
                ""
            ).lower()



            if project_type:


                if project_type == "mobile":

                    if any(
                        item in pattern_name
                        for item in [
                            "flutter",
                            "firebase",
                            "react native"
                        ]
                    ):

                        context_match = 1



                elif project_type == "web":

                    if any(
                        item in pattern_name
                        for item in [
                            "fastapi",
                            "django",
                            "react",
                            "docker",
                            "postgresql"
                        ]
                    ):

                        context_match = 1



                elif project_type == "ai":

                    if any(
                        item in pattern_name
                        for item in [
                            "tensorflow",
                            "pytorch",
                            "ai",
                            "model"
                        ]
                    ):

                        context_match = 1



            decision_score = (

                success_rate * 0.25

                +

                priority_score * 0.15

                +

                confidence * 0.10

                +

                memory_score * 0.15

                +

                adaptive_decision_score * 0.15

                +

                context_match * 0.20

                +

                recency * 0.05

                -

                failure_penalty

            )


            ranked.append({

                **pattern,

                "context_match": context_match,

                "decision_score": round(

                    decision_score,

                    3

                )

            })



        return sorted(

            ranked,

            key=lambda x: x["decision_score"],

            reverse=True

        )