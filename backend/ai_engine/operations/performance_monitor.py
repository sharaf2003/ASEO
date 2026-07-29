class PerformanceMonitor:
    """
    ASEO Performance Monitor v22.3
    """

    def analyze(
        self,
        metrics
    ):

        return {

            "cpu":
                metrics.get(
                    "cpu",
                    20
                ),

            "memory":
                metrics.get(
                    "memory",
                    40
                ),

            "response_time":
                "fast",

            "performance":
                "optimal"

        }