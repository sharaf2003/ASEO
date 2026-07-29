class ResultAnalyzer:
    """
    ASEO Result Analyzer v20.3
    """

    def analyze(
        self,
        result
    ):

        quality = result.get(
            "quality",
            0
        )

        success = quality >= 80


        return {

            "success":
                success,

            "quality":
                quality,

            "evaluation":
                "positive" if success else "negative"

        }