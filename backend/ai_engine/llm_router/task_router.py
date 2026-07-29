class TaskRouter:
    """
    ASEO Task Router v16
    """



    def classify(
        self,
        task
    ):


        text = task.lower()



        # Security must be checked first
        # because words like "issue" may exist
        # inside security requests

        if "security" in text:

            return "security"




        if any(

            word in text

            for word in [

                "architecture",

                "design",

                "system"

            ]

        ):

            return "architecture"




        if any(

            word in text

            for word in [

                "code",

                "api",

                "function",

                "implement"

            ]

        ):

            return "coding"




        if any(

            word in text

            for word in [

                "error",

                "bug",

                "fix",

                "issue"

            ]

        ):

            return "debugging"




        return "general"