class PatternScorer:
    """
    ASEO Pattern Reliability Scorer v4

    Evaluates engineering pattern reliability.

    Factors:

    Initial Confidence
    +
    Learning Feedback
    +
    Success History
    +
    Usage Experience
    +
    Failure Penalty
    """



    def score(
        self,
        pattern
    ):


        confidence = pattern.get(
            "confidence",
            0
        ) or 0



        usage_count = pattern.get(
            "usage_count",
            0
        ) or 0



        success_rate = pattern.get(
            "success_rate",
            0
        ) or 0



        failure_rate = pattern.get(
            "failure_rate",
            0
        ) or 0



        success_count = pattern.get(
            "success_count",
            0
        ) or 0



        failure_count = pattern.get(
            "failure_count",
            0
        ) or 0





        # =================================
        # Experience Factor
        # =================================

        #
        # كلما زاد استخدام الـ pattern
        # تزيد الخبرة تدريجياً
        #

        usage_factor = min(
            usage_count / 50,
            1.0
        )






        # =================================
        # Learning Factor
        # =================================

        #
        # Pattern جديد:
        # يعتمد على confidence
        #
        # Pattern لديه feedback:
        # يعتمد على النجاح الحقيقي
        #

        if success_count == 0:

            learning_factor = confidence

        else:

            learning_factor = success_rate






        # =================================
        # Reliability Score
        # =================================


        score = (

            # Initial knowledge

            (confidence * 0.35)


            +


            # Real learning experience

            (learning_factor * 0.45)


            +


            # Usage experience

            (usage_factor * 0.20)


            -


            # Failure penalty

            (failure_rate * 0.30)

        )





        score = max(

            0,

            min(

                score,

                1

            )

        )







        # =================================
        # Trust Classification
        # =================================


        if score >= 0.85:

            level = "trusted"



        elif score >= 0.65:

            level = "validated"



        else:

            level = "experimental"







        return {


            "pattern":

                pattern.get(
                    "name"
                ),



            "score":

                round(
                    score,
                    3
                ),



            "trust_level":

                level,



            "metrics":

            {

                "confidence":

                    confidence,



                "usage_count":

                    usage_count,



                "success_count":

                    success_count,



                "failure_count":

                    failure_count,



                "success_rate":

                    success_rate,



                "failure_rate":

                    failure_rate

            }

        }