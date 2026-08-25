from app.intelligence.optimization.adaptive_optimizer import (
    AdaptiveArchitectureOptimizer
)


class ArchitectureDecisionEngine:
    """
    Combines reasoning, memory, performance and feedback
    to produce adaptive architecture decision.
    """


    def __init__(self):

        self.optimizer = (
            AdaptiveArchitectureOptimizer()
        )


    def decide(
        self,
        reasoning_result: dict,
        memory_data: dict | None = None,
        feedback_score: float = 0,
        performance_confidence: float = 0,
        evolution_score: float = 0.5,
        candidates: list | None = None,
        evolution_memory: dict | None = None
    ) -> dict:


        recommendation = (
            reasoning_result
            .get(
                "recommendation",
                {}
            )
        )


        candidate_ranking = []


        if candidates:

            for candidate in candidates:


                architecture_name = candidate.get(
                    "name"
                )


                reasoning_score = candidate.get(
                    "final_score",
                    0
                )


                evolution_score_candidate = 0.5


                if evolution_memory:

                    memory = evolution_memory.get(
                        architecture_name,
                        {}
                    )


                    evolution_score_candidate = memory.get(
                        "success_rate",
                        0.5
                    )


                adaptive_score = (

                    reasoning_score * 0.5

                    +

                    evolution_score_candidate * 0.5

                )


                candidate_ranking.append({

                    "architecture":
                        architecture_name,


                    "reasoning_score":
                        reasoning_score,


                    "evolution_score":
                        evolution_score_candidate,


                    "score":
                        adaptive_score

                })


        reasoning_score = recommendation.get(
            "score",
            0
        )


        memory_score = 0

        historical_success = 0

        memory_strength = 0



        if memory_data:


            memory_score = memory_data.get(
                "memory_score",
                0
            )


            historical_success = memory_data.get(
                "success_score",
                0
            )


            memory_strength = memory_data.get(
                "memory_strength",
                0
            )



        adaptive_weights = (
            self.optimizer.calculate_weights(
                performance_confidence,
                memory_strength
            )
        )



        final_score = (

            reasoning_score *
            adaptive_weights["reasoning"]

            +

            memory_score *
            adaptive_weights["memory"]

            +

            historical_success *
            adaptive_weights["performance"]

            +

            feedback_score *
            adaptive_weights["feedback"]

            +

            memory_strength * 0.10

        )


        # Apply evolution learning penalty

        final_score = (
            final_score *
            evolution_score
        )



        final_score = min(
            final_score,
            1.0
        )

        # Adaptive architecture switching
        if evolution_score < 0.3 or feedback_score < 0.3:

            alternatives = recommendation.get(
                "alternatives",
                []
            )

            if alternatives:

                best_alternative = max(
                    alternatives,
                    key=lambda x: x.get(
                        "score",
                        0
                    )
                )

                recommendation["recommended_architecture"] = (
                    best_alternative.get(
                        "name"
                    )
                )

                final_score = max(
                    best_alternative.get(
                        "score",
                        0
                    ),
                    final_score
                )

            if candidate_ranking:

                best_candidate = max(
                    candidate_ranking,
                    key=lambda x:x["score"]
                )


                recommendation[
                    "recommended_architecture"
                ] = best_candidate["architecture"]

        return {


            "architecture":

                recommendation.get(
                    "recommended_architecture"
                ),



            "reasoning_score":

                round(
                    reasoning_score,
                    2
                ),



            "memory_score":

                round(
                    memory_score,
                    2
                ),



            "historical_success":

                round(
                    historical_success,
                    2
                ),



            "memory_strength":

                round(
                    memory_strength,
                    2
                ),



            "performance_confidence":

                round(
                    performance_confidence,
                    2
                ),



            "feedback_score":

                round(
                    feedback_score,
                    2
                ),



            "adaptive_weights":

                adaptive_weights,


            "evolution_score":

                round(
                    evolution_score,
                    2
                ),

            
            "candidate_ranking":
                candidate_ranking,

            "final_decision_score":

                round(
                    final_score,
                    2
                )

        }