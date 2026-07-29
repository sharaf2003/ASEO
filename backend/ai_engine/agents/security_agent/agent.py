import time

from .security_scanner import SecurityScanner





class SecurityAgent:
    """
    ASEO Security Agent v2.0

    Performs security analysis,
    vulnerability scanning and
    security validation.
    """



    def __init__(self):


        self.scanner = SecurityScanner()



        self.agent_info = {


            "name":

                "Security Agent",



            "version":

                "2.0"

        }





    def run(
        self,
        project_path
    ):


        start = time.time()



        try:


            issues = self.scanner.scan(

                project_path

            )





            status = "passed"





            if issues:


                status = "warning"







            return {


                "status":

                    status,



                "agent_info":

                    self.agent_info,



                "security":

                    {


                        "issues":

                            issues,


                        "issues_count":

                            len(issues)

                    },



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