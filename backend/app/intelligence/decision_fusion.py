class DecisionFusion:

    """
    Adaptive Decision Fusion Engine

    Combines multiple intelligence sources:

    - Pattern ranking score
    - Previous architecture similarity
    - Historical success
    - Usage experience

    Produces:
    - Decision confidence
    - Decision quality
    - Explanation
    """



    def calculate_confidence(

        self,

        pattern_score: float,

        similarity_score: float = 0,

        success_score: float = 0,

        usage_count: int = 0

    ) -> float:


        # Normalize values

        pattern_score = max(

            min(pattern_score, 1),

            0

        )


        similarity_normalized = max(

            min(similarity_score / 100, 1),

            0

        )


        success_score = max(

            min(success_score, 1),

            0

        )



        # Usage experience bonus

        usage_bonus = min(

            usage_count / 100,

            0.1

        )



        # Adaptive weights

        pattern_weight = 0.45

        similarity_weight = 0.25

        success_weight = 0.20

        usage_weight = 0.10



        confidence = (

            pattern_score * pattern_weight

            +

            similarity_normalized * similarity_weight

            +

            success_score * success_weight

            +

            usage_bonus * usage_weight

        )



        return round(

            min(confidence, 1),

            2

        )

    # =============================================
    # Final Decision Score Fusion
    # =============================================

    def calculate_final_decision_score(

        self,

        pattern_score: float = 0,

        memory_score: float = 0,

        confidence_score: float = 0

    ) -> float:


        # Normalize inputs

        pattern_score = max(
            min(pattern_score, 1),
            0
        )


        memory_score = max(
            min(memory_score, 1),
            0
        )


        confidence_score = max(
            min(confidence_score, 1),
            0
        )


        # Adaptive fusion weights

        pattern_weight = 0.4

        memory_weight = 0.4

        confidence_weight = 0.2



        final_score = (

            pattern_score * pattern_weight

            +

            memory_score * memory_weight

            +

            confidence_score * confidence_weight

        )


        return round(

            min(final_score, 1),

            2

        )



    # =============================================
    # Decision Quality
    # =============================================


    def quality(

        self,

        confidence: float

    ):


        if confidence >= 0.85:

            return "high"


        if confidence >= 0.6:

            return "medium"


        return "low"



    # =============================================
    # Explain Decision
    # =============================================


    def explain(

        self,

        pattern_score,

        similarity_score,

        success_score,

        usage_count=0

    ):


        reasons = []



        if pattern_score >= 0.8:


            reasons.append(

                "Strong knowledge pattern"

            )



        if similarity_score >= 50:


            reasons.append(

                "Similar previous successful project"

            )



        if success_score >= 0.8:


            reasons.append(

                "High historical success"

            )



        if usage_count > 5:


            reasons.append(

                f"Used in {usage_count} successful executions"

            )



        if not reasons:


            reasons.append(

                "Limited historical evidence"

            )



        return reasons