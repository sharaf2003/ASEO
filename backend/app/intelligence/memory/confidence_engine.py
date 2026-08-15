class ConfidenceEngine:


    """
    Calculates confidence level
    for AI decisions
    """


    def calculate_confidence(

        self,

        similarity_score: float,

        success_score: float,

        usage_count: int,

        memory_score: float,

        recency: float,

        feedback_score: float = 0,

        adaptive_memory_score: float = 0

    ) -> float:


        similarity_weight = 0.25

        success_weight = 0.20

        usage_weight = 0.15

        memory_weight = 0.20

        recency_weight = 0.10

        feedback_weight = 0.05

        adaptive_memory_weight = 0.05



        usage_factor = min(

            usage_count / 10,

            1

        )



        confidence = (

            similarity_score *
            similarity_weight

            +

            success_score *
            success_weight

            +

            usage_factor *
            usage_weight

            +

            memory_score *
            memory_weight

            +

            recency *
            recency_weight

            +

            feedback_score *
            feedback_weight

            +

            adaptive_memory_score *
            adaptive_memory_weight

        )



        return round(

            max(

                min(confidence, 1),

                0

            ),

            2

        )