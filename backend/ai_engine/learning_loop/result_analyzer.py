class ResultAnalyzer:
    """
    ASEO Result Analyzer v21

    Intelligent quality evaluation layer.

    Evaluates:
    - Decision confidence
    - Evidence quality
    - Pattern usage
    - Execution completeness
    """


    def analyze(
        self,
        result
    ):


        score = 0



        # 1. Decision quality

        decision = result.get(
            "decision",
            {}
        )

        if isinstance(decision, str):

            decision = {
                "action": decision,
                "confidence": 0
            }


        confidence = decision.get(
            "confidence",
            0
        )


        score += confidence * 50





        # 2. Evidence evaluation

        evidence = decision.get(
            "evidence",
            result.get(
                "evidence",
                []
            )
        )


        if evidence:

            score += 20





        # 3. Pattern intelligence

        patterns = decision.get(
            "patterns",
            result.get(
                "patterns",
                []
            )
        )


        if patterns:

            score += 20



        # 4. Requirement completion

        if result.get(
            "requirement"
        ):

            score += 10





        quality = round(
            min(score,100)
        )



        success = quality >= 80



        return {

            "success":
                success,


            "quality":
                quality,


            "evaluation":
                "positive"
                if success
                else "negative"

        }