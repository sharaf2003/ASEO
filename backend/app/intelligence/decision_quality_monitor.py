class DecisionQualityMonitor:

    """
    ASEO Decision Quality Monitor

    Evaluates if an agent decision was successful.

    Responsibilities:

    - Measure decision quality
    - Analyze feedback
    - Generate improvement suggestions
    """



    def evaluate(

        self,

        decision,

        feedback

    ) -> dict:


        reasons = []

        score = 0



        # =============================================
        # Feedback Evaluation
        # =============================================


        feedback_score = getattr(

            feedback,

            "score",

            0

        )


        score += feedback_score * 0.7



        if feedback_score >= 0.8:


            reasons.append(

                "Execution feedback was successful"

            )


        else:


            reasons.append(

                "Execution feedback requires improvement"

            )



        # =============================================
        # Decision Confidence Evaluation
        # =============================================


        confidence = None



        if isinstance(decision, dict):


            confidence = decision.get(

                "confidence"

            )



        if confidence is not None:


            score += confidence * 0.3



            if confidence >= 0.8:


                reasons.append(

                    "Decision had strong confidence"

                )


            else:


                reasons.append(

                    "Decision confidence was moderate"

                )


        else:


            # No decision confidence available

            score += feedback_score * 0.3


            reasons.append(

                "Quality measured from execution feedback"

            )



        quality = round(

            min(score, 1),

            2

        )



        return {

            "quality_score": quality,

            "quality_level":

                self.get_level(

                    quality

                ),

            "reasons": reasons

        }



    # =============================================
    # Quality Classification
    # =============================================


    def get_level(

        self,

        score

    ):


        if score >= 0.85:


            return "excellent"



        if score >= 0.65:


            return "good"



        return "needs_improvement"