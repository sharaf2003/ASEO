class ReportGenerator:
    """
    ASEO Quality Report Generator v1
    """



    def generate(
        self,
        results
    ):


        errors = [

            item

            for item in results

            if item["status"] == "failed"

        ]



        return {


            "status":

                "passed"

                if not errors

                else "failed",



            "files_checked":

                len(results),



            "errors":

                len(errors),



            "details":

                results

        }