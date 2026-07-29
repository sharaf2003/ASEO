import time


from .reviewer import SeniorReviewer





class SeniorReviewAgent:


    def __init__(self):


        self.reviewer = SeniorReviewer()



        self.agent_info = {


            "name":

            "Senior Code Review Agent",


            "version":

            "1.0"

        }





    def run(self, project_path):


        start = time.time()



        result = self.reviewer.review(

            project_path

        )



        status = "passed"



        if result["issues"]:

            status = "warning"





        return {


            "status":

            status,


            "agent_info":

            self.agent_info,


            "review":

            result,


            "processing_time":

            round(

                time.time()-start,

                3

            )

        }