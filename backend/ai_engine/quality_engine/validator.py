class QualityValidator:
    """
    ASEO Quality Validation Engine v15
    """



    def __init__(
        self,
        runner
    ):

        self.runner = runner





    def validate(
        self,
        tests
    ):


        execution = self.runner.run(

            tests

        )



        passed = 0



        for result in execution["results"]:


            if result["status"] == "passed":

                passed += 1





        total = execution["tests_run"]



        score = 0



        if total > 0:


            score = int(

                (passed / total)

                *

                100

            )





        return {


            "tests_run":

                total,


            "passed":

                passed,


            "failed":

                total - passed,


            "quality_score":

                score,


            "status":

                "approved"

                if score >= 80

                else

                "rejected"

        }