class RepairLoop:
    """
    ASEO Repair Loop v1

    Controls repair attempts.
    """



    def __init__(
        self,
        max_attempts=3
    ):

        self.max_attempts = max_attempts





    def should_continue(
        self,
        attempt,
        report
    ):


        if report.get("status") == "passed":

            return False



        if attempt >= self.max_attempts:

            return False



        return True