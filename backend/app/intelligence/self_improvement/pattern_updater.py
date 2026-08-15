class PatternUpdater:


    """
    Updates knowledge pattern priority
    automatically based on feedback.
    """



    def __init__(

        self,

        repository=None

    ):

        self.repository = repository



    def apply_failure_penalty(

        self,

        pattern_id: int,

        penalty_score: float = 0.05

    ) -> dict:



        if not self.repository:

            return {

                "updated": False,

                "reason": "Repository not available"

            }



        pattern = self.repository.get_pattern_by_id(

            pattern_id

        )



        if not pattern:

            return {

                "updated": False,

                "reason": "Pattern not found"

            }



        current_score = (

            pattern.priority_score

        )



        new_score = (

            current_score

            -

            penalty_score

        )


        MIN_PRIORITY = 0.1


        if new_score < MIN_PRIORITY:

            new_score = MIN_PRIORITY



        updated_pattern = (

            self.repository.update_priority(

                pattern_id,

                round(

                    new_score,

                    2

                )

            )

        )



        return {


            "pattern_id": pattern_id,


            "old_score": current_score,


            "penalty": penalty_score,


            "new_score": round(

                new_score,

                2

            ),


            "updated": updated_pattern is not None


        }