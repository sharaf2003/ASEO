from datetime import datetime



class OptimizationTracker:
    """
    ASEO Optimization Tracker v21.5
    """

    def track(
        self,
        before,
        after
    ):


        return {

            "quality_before":
                before,

            "quality_after":
                after,

            "improved":
                after > before,

            "timestamp":
                datetime.now().isoformat()

        }