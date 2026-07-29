class ErrorAnalyzer:
    """
    ASEO Error Analyzer v16
    """



    def analyze(
        self,
        error
    ):


        error_text = error.lower()



        if "database" in error_text:

            return {

                "type":
                    "database_error",


                "cause":
                    "Database connection problem",


                "severity":
                    "high"

            }



        if "import" in error_text:

            return {

                "type":
                    "dependency_error",


                "cause":
                    "Missing dependency or wrong import",


                "severity":
                    "medium"

            }



        return {

            "type":
                "unknown_error",


            "cause":
                "Needs investigation",


            "severity":
                "medium"

        }