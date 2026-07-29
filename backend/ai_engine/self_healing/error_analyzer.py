class ErrorAnalyzer:
    """
    ASEO Error Analyzer v21.4
    """

    def analyze(
        self,
        error
    ):


        if "database" in error.lower():

            return {

                "type":
                    "database_error",

                "cause":
                    "Database configuration problem",

                "severity":
                    "high"

            }


        elif "import" in error.lower():

            return {

                "type":
                    "dependency_error",

                "cause":
                    "Missing dependency",

                "severity":
                    "medium"

            }


        return {

            "type":
                "unknown_error",

            "cause":
                "Unknown cause",

            "severity":
                "low"

        }