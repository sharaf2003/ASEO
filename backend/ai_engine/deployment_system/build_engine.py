class BuildEngine:
    """
    ASEO Build Engine v22.2
    """

    def build(
        self,
        repository
    ):

        return {

            "repository":
                repository["repository"],

            "build":
                "successful",

            "artifacts":
                5

        }