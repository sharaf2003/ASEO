class ErrorAnalyzer:
    """
    ASEO Error Analyzer v1
    """



    def analyze(
        self,
        report
    ):


        errors = []



        for item in report.get(
            "details",
            []
        ):


            if item["status"] == "failed":


                errors.append(
                    {

                        "file":

                            item["file"],


                        "error":

                            item["error"]

                    }

                )



        return errors