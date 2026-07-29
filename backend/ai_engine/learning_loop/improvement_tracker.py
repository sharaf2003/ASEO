class ImprovementTracker:
    """
    ASEO Improvement Tracker v20.3
    """

    def __init__(self):

        self.history = []



    def track(
        self,
        before,
        after
    ):


        record = {

            "before":
                before,

            "after":
                after,

            "improved":
                after > before

        }


        self.history.append(record)


        return record