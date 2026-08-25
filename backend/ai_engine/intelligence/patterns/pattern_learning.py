from datetime import datetime


class PatternLearning:
    """
    ASEO Pattern Evolution Engine v2

    Responsible for:

    Experience feedback
    +
    Pattern evolution
    +
    Confidence adaptation
    +
    Lifecycle management
    """



    def update(
        self,
        pattern,
        success,
        score=0
    ):


        # Usage counter

        pattern["usage_count"] = (
            pattern.get(
                "usage_count",
                0
            )
            + 1
        )



        if success:

            pattern["success_count"] = (

                pattern.get(
                    "success_count",
                    0
                )
                + 1

            )


        else:

            pattern["failure_count"] = (

                pattern.get(
                    "failure_count",
                    0
                )
                + 1

            )




        usage = pattern["usage_count"]


        success_rate = (

            pattern["success_count"]
            /
            usage

        )


        failure_rate = (

            pattern["failure_count"]
            /
            usage

        )



        pattern["success_rate"] = round(
            success_rate,
            3
        )


        pattern["failure_rate"] = round(
            failure_rate,
            3
        )




        #
        # Evolution score
        #

        confidence = pattern.get(
            "confidence",
            0
        )


        evolution_score = (

            confidence * 0.5

            +

            success_rate * 0.3

            +

            (score / 100) * 0.2

        )



        pattern["evolution_score"] = round(
            evolution_score,
            3
        )




        #
        # Lifecycle
        #

        if evolution_score >= 0.85:

            pattern["status"] = "trusted"


        elif evolution_score >= 0.60:

            pattern["status"] = "learning"


        else:

            pattern["status"] = "weak"




        pattern["last_evaluated"] = (
            datetime.utcnow()
            .isoformat()
        )



        return pattern