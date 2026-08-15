class PatternPenaltyEngine:


    """
    Calculates penalty amount
    after failed executions.
    """



    def calculate_penalty(

        self,

        current_score: float,

        failure_count: int = 1

    ) -> float:


        base_penalty = 0.05


        penalty = (

            base_penalty

            *

            failure_count

        )


        # لا نسمح بعقوبة أكبر من الدرجة الحالية

        if penalty > current_score:

            penalty = current_score



        return round(

            penalty,

            2

        )