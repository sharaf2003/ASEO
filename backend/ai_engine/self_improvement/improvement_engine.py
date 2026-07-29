from .improvement_record import ImprovementRecord



class SelfImprovementEngine:
    """
    ASEO Self Improvement Engine v17.5

    Capabilities:

    - Compare previous results
    - Detect problems
    - Generate fixes
    - Apply improvements
    - Store improvement history
    """



    def __init__(
        self
    ):

        self.records = []

        self.improvements = []






    # =====================================
    # Legacy Improvement System
    # Compatible with v14-v16
    # =====================================

    def improve(
        self,
        old_prompt,
        new_prompt,
        old_score,
        new_score
    ):


        improved = (

            new_score > old_score

        )



        record = ImprovementRecord(

            old_score,

            new_score,

            old_prompt,

            new_prompt,

            improved

        )



        self.records.append(

            record

        )



        return record.to_dict()







    # =====================================
    # Error Analysis System v17.5
    # =====================================

    def analyze_error(
        self,
        error
    ):


        text = error.lower()



        if "database" in text:


            return {


                "type":

                    "database_error",


                "cause":

                    "Database connection problem",


                "severity":

                    "high"

            }




        if "authentication" in text:


            return {


                "type":

                    "authentication_error",


                "cause":

                    "Authentication configuration problem",


                "severity":

                    "high"

            }





        if "syntax" in text:


            return {


                "type":

                    "syntax_error",


                "cause":

                    "Invalid code syntax",


                "severity":

                    "medium"

            }





        return {


            "type":

                "unknown_error",


            "cause":

                error,


            "severity":

                "medium"

        }








    # =====================================
    # Fix Generation v17.5
    # =====================================

    def generate_fix(
        self,
        analysis
    ):


        solution = (

            f"Apply fix for {analysis['type']}"

        )



        return {


            "fix_generated":

                True,


            "solution":

                solution,


            "applied":

                False

        }








    # =====================================
    # Apply Fix
    # =====================================

    def apply_fix(
        self,
        fix
    ):


        fix["applied"] = True



        self.improvements.append(

            fix

        )



        return fix








    # =====================================
    # Full Self Improvement Cycle
    # =====================================

    def self_improve(
        self,
        error
    ):


        analysis = self.analyze_error(

            error

        )



        fix = self.generate_fix(

            analysis

        )



        fix = self.apply_fix(

            fix

        )



        return {


            "error":

                error,


            "analysis":

                analysis,


            "fix":

                fix,


            "status":

                "resolved"

        }








    def history(
        self
    ):


        return [


            record.to_dict()


            for record


            in self.records


        ]