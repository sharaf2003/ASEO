import time

from .quality_scanner import QualityScanner
from .quality_fixer import QualityFixer





class QualityAgent:
    """
    ASEO Quality Agent v2.0

    Performs code quality analysis,
    automatic fixes and validation.
    """



    def __init__(self):


        self.scanner = QualityScanner()


        self.fixer = QualityFixer()



        self.agent_info = {


            "name":

                "Quality Agent",



            "version":

                "2.0"

        }





    def run(
        self,
        project_path
    ):


        start = time.time()



        try:


            result = self.scanner.scan(

                project_path

            )



            fixes = []





            for issue in result.get(
                "issues",
                []
            ):


                if issue.get(
                    "issue"
                ) == "Missing documentation":



                    fix = self.fixer.fix_documentation(

                        issue["file"]

                    )


                    fixes.append(

                        fix

                    )







            final_result = self.scanner.scan(

                project_path

            )





            status = "passed"



            if final_result.get(
                "issues"
            ):


                status = "warning"







            return {


                "status":

                    status,



                "agent_info":

                    self.agent_info,



                "quality":

                    final_result,



                "fixes":

                    fixes,



                "processing_time":

                    round(

                        time.time() - start,

                        3

                    )

            }






        except Exception as error:



            return {


                "status":

                    "failed",



                "agent_info":

                    self.agent_info,



                "error":

                    str(error),



                "processing_time":

                    round(

                        time.time() - start,

                        3

                    )

            }