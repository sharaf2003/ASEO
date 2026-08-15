class PatternRanker:

    """
    ASEO Pattern Ranking Engine

    Responsible for:

    - Ranking knowledge patterns
    - Calculating knowledge score
    - Selecting best experiences
    - Explaining decisions
    """



    def __init__(

        self

    ):

        pass



    # =============================================
    # Rank Patterns
    # =============================================


    def rank(

        self,

        patterns: list,

        context: dict | None = None

    ) -> list:


        ranked = []


        for pattern in patterns:


            score = self.calculate_score(

                pattern,

                context

            )


            reasons = self.generate_reason(

                pattern,

                context

            )


            ranked.append(

                {

                    "pattern": pattern,

                    "score": score,

                    "reason": reasons,

                    "reasons": reasons

                }

            )


        ranked.sort(

            key=lambda item:

                item["score"],

            reverse=True

        )


        return ranked



    # =============================================
    # Calculate Knowledge Score
    # =============================================


    def calculate_score(

        self,

        pattern,

        context=None

    ):


        score = 0



        # Success rate weight

        success_rate = self.get_value(

            pattern,

            "success_rate",

            0

        )



        score += (

            float(success_rate) / 100

        ) * 0.5



        # Usage weight

        usage_count = self.get_value(

            pattern,

            "usage_count",

            0

        )



        if usage_count > 0:


            score += min(

                float(usage_count) / 100,

                0.2

            )



        # Context matching

        pattern_layer = self.get_value(

            pattern,

            "layer",

            None

        )


        context_layer = None


        if context:

            context_layer = context.get(

                "layer"

            )



        if (

            context_layer

            and

            pattern_layer

            and

            context_layer == pattern_layer

        ):


            score += 0.3



        return round(

            min(score, 1),

            2

        )



    # =============================================
    # Explain Decision
    # =============================================


    def generate_reason(

        self,

        pattern,

        context=None

    ) -> list:


        reasons = []



        success_rate = self.get_value(

            pattern,

            "success_rate",

            0

        )



        usage_count = self.get_value(

            pattern,

            "usage_count",

            0

        )



        pattern_layer = self.get_value(

            pattern,

            "layer",

            None

        )



        if success_rate >= 90:


            reasons.append(

                "High success rate"

            )


        elif success_rate > 0:


            reasons.append(

                "Acceptable success rate"

            )

        else:


            reasons.append(

                "No success history"

            )



        if usage_count > 1:


            reasons.append(

                f"Used in {usage_count} executions"

            )


        else:


            reasons.append(

                "New knowledge pattern"

            )



        if context:


            if context.get("layer") == pattern_layer:


                reasons.append(

                    "Context matched"

                )



        return reasons



    # =============================================
    # Safe Value Extractor
    # =============================================


    def get_value(

        self,

        obj,

        key,

        default=None

    ):


        if obj is None:

            return default



        if isinstance(obj, dict):


            return obj.get(

                key,

                default

            )



        return getattr(

            obj,

            key,

            default

        )