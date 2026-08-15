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
        performance_confidence: float = 0
    ) -> dict:


        recommendation = (
            reasoning_result
            .get(
                "recommendation",
                {}
            )
        )


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



        final_score = min(
            final_score,
            1.0
        )



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



            "final_decision_score":

                round(
                    final_score,
                    2
                )

        }