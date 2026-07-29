import time

from .reviewer import APIReviewer





class APIValidatorAgent:
    """
    ASEO API Contract Validator Agent v2.0

    Responsible for validating REST API
    contracts, endpoints, API design,
    response models and conventions.
    """



    def __init__(self):


        self.reviewer = APIReviewer()



        self.agent_info = {


            "name":

                "API Contract Validator Agent",



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



                "api_review":

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