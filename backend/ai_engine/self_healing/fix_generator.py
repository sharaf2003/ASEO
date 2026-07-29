class FixGenerator:
    """
    ASEO Fix Generator v21.4
    """

    def generate(
        self,
        analysis
    ):


        fixes = {

            "database_error":
                "Update database configuration",

            "dependency_error":
                "Install missing dependency",

            "unknown_error":
                "Review source code"

        }


        return {

            "fix_generated":
                True,

            "solution":
                fixes.get(

                    analysis["type"],

                    "Manual review"

                )

        }