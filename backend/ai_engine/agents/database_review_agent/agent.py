import time

from .reviewer import DatabaseReviewer





class DatabaseReviewAgent:
    """
    ASEO Database Design Review Agent v2.0

    Responsible for analyzing database models,
    tables, primary keys and database structure.
    """



    def __init__(self):


        self.reviewer = DatabaseReviewer()



        self.agent_info = {


            "name":

                "Database Design Review Agent",



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



                "database":

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