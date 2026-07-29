import time

from .reviewer import ArchitectureReviewer





class ArchitectureAgent:
    """
    ASEO Architecture Review Agent v2.0

    Responsible for analyzing software architecture,
    detecting patterns, layers and architecture issues.
    """



    def __init__(self):


        self.reviewer = ArchitectureReviewer()



        self.agent_info = {


            "name":

                "Architecture Review Agent",



            "version":

                "2.0"

        }





    def run(
        self,
        project_path
    ):


        start = time.time()



        try:


            result = self.reviewer.review(

                project_path

            )





            status = "passed"




            if (

                result.get("issues")

                or

                result.get("recommendations")

            ):


                status = "warning"







            return {


                "status":

                    status,



                "agent_info":

                    self.agent_info,



                "architecture":

                    result,



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