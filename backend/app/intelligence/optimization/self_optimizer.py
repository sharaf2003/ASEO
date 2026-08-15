from app.repositories.optimization_repository import OptimizationRepository


class SelfOptimizer:

    """
    ASEO Self Optimization Engine

    Responsibilities:

    - Analyze decision quality
    - Improve knowledge pattern weights
    - Increase successful patterns
    - Reduce weak patterns
    - Save optimization history
    """


    def __init__(

        self,

        db=None

    ):

        self.db = db

        self.repository = OptimizationRepository(

            db=db

        )



    # =============================================
    # Optimize Knowledge Pattern
    # =============================================


    def optimize(

        self,

        patterns: list,

        quality_result: dict

    ) -> dict:


        updated_patterns = []


        if not patterns:

            return {

                "optimized": False,

                "reason": "No patterns available",

                "updated_patterns": []

            }



        quality_score = quality_result.get(

            "quality_score",

            0

        )



        for pattern in patterns:


            if not isinstance(pattern, dict):

                continue



            old_score = pattern.get(

                "priority_score",

                0.5

            )



            # =============================================
            # Calculate New Priority Score
            # =============================================


            if quality_score >= 0.85:


                new_score = min(

                    old_score + 0.05,

                    1

                )


                reason = (

                    "Increased priority after successful execution"

                )



            elif quality_score < 0.5:


                new_score = max(

                    old_score - 0.05,

                    0

                )


                reason = (

                    "Decreased priority after poor execution"

                )



            else:


                new_score = old_score


                reason = (

                    "Priority unchanged due to average quality"

                )



            new_score = round(

                new_score,

                2

            )


            pattern["priority_score"] = new_score



            # =============================================
            # Extract Pattern ID
            # =============================================


            pattern_id = self.extract_pattern_id(

                pattern

            )



            # =============================================
            # Update Knowledge Pattern Weight
            # =============================================


            if pattern_id:


                update_result = self.repository.update_pattern_weight(

                    pattern_id,

                    new_score,

                    reason

                )


            else:


                update_result = {

                    "updated": False,

                    "reason": "Pattern ID not available"

                }



            # =============================================
            # Save Optimization History
            # =============================================


            history_result = self.repository.save_history(

                {

                    "pattern_id": pattern_id,

                    "pattern": pattern.get(

                        "pattern",

                        pattern.get(

                            "name",

                            "unknown"

                        )

                    ),

                    "old_score": old_score,

                    "new_score": new_score,

                    "quality_score": quality_score,

                    "reason": reason

                }

            )



            pattern["optimization_update"] = update_result


            pattern["history_update"] = history_result



            updated_patterns.append(

                pattern

            )



        return {

            "optimized": True,

            "quality_score": quality_score,

            "updated_patterns": updated_patterns

        }



    # =============================================
    # Extract Pattern ID Safely
    # =============================================


    def extract_pattern_id(

        self,

        pattern: dict

    ):


        pattern_id = pattern.get(

            "id"

        )


        if pattern_id:

            return pattern_id



        inner_pattern = pattern.get(

            "pattern"

        )



        if isinstance(inner_pattern, dict):


            pattern_id = inner_pattern.get(

                "id"

            )


            if pattern_id:

                return pattern_id



        return pattern.get(

            "pattern_id"

        )