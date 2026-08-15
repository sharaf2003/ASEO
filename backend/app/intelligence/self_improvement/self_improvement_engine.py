from app.intelligence.self_improvement.failure_analyzer import (
    FailureAnalyzer
)

from app.intelligence.self_improvement.pattern_penalty import (
    PatternPenaltyEngine
)

from app.intelligence.self_improvement.pattern_updater import (
    PatternUpdater
)



class SelfImprovementEngine:


    """
    Controls self improvement cycle.

    Connects:
    - Failure Analysis
    - Penalty Calculation
    - Pattern Updating
    """



    def __init__(

        self,

        repository=None

    ):


        self.failure_analyzer = FailureAnalyzer()


        self.penalty_engine = PatternPenaltyEngine()


        self.pattern_updater = PatternUpdater(

            repository

        )



    def process_failure(

        self,

        execution_result: dict,

        architecture_result: list

    ) -> dict:

        architecture_decisions = architecture_result.get(
            "architecture_decisions",
            []
        )



        analysis = self.failure_analyzer.analyze(

            execution_result,

            architecture_decisions

        )



        if not analysis.get("failed"):


            return {

                "updated": False,

                "reason": "Execution succeeded"

            }



        updates = []



        for failure in analysis.get(

            "failures",

            []

        ):


            pattern_id = failure.get(

                "pattern_id"

            )


            if not pattern_id:

                continue



            pattern = self.pattern_updater.repository.get_pattern_by_id(
                pattern_id
            )


            current_score = pattern.priority_score if pattern else 0.5


            penalty = self.penalty_engine.calculate_penalty(

                current_score=current_score,

                failure_count=1

            )



            result = self.pattern_updater.apply_failure_penalty(

                pattern_id,

                penalty

            )


            updates.append(result)



        return {


            "updated": True,


            "failures": analysis.get(

                "failures"

            ),


            "updates": updates

        }