from .request_manager import RequestManager

from .execution_pipeline import ExecutionPipeline

from .report_generator import ReportGenerator





class AutonomousController:
    """
    ASEO Autonomous Controller v20.0
    """



    def __init__(self):

        self.requests = RequestManager()

        self.pipeline = ExecutionPipeline()

        self.reports = ReportGenerator()





    def run(
        self,
        requirement
    ):


        request = self.requests.create_request(

            requirement

        )


        execution = self.pipeline.execute(

            requirement

        )


        report = self.reports.generate(

            execution

        )


        return {


            "request":

                request,


            "execution":

                execution,


            "report":

                report

        }