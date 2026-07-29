import time





class ExecutionTracker:
    """
    ASEO Execution Tracker v2.0

    Tracks pipeline execution,
    agent status and performance.
    """



    def __init__(self):

        self.steps = []





    def add_step(
        self,
        name,
        status
    ):


        self.steps.append(

            {

                "step":

                    name,


                "status":

                    status,


                "timestamp":

                    time.time()

            }

        )





    def get_completed_steps(
        self
    ):


        return [

            step

            for step in self.steps

            if step["status"] == "completed"

            or step["status"] == "success"

            or step["status"] == "passed"

        ]





    def get_failed_steps(
        self
    ):


        return [

            step

            for step in self.steps

            if step["status"] == "failed"

        ]





    def get_warning_steps(
        self
    ):


        return [

            step

            for step in self.steps

            if step["status"] == "warning"

        ]





    def report(
        self
    ):


        return {


            "steps":

                self.steps,


            "summary":

                {

                    "total":

                        len(self.steps),


                    "completed":

                        len(

                            self.get_completed_steps()

                        ),


                    "failed":

                        len(

                            self.get_failed_steps()

                        ),


                    "warnings":

                        len(

                            self.get_warning_steps()

                        )

                }

        }