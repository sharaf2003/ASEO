import time



from .project_scanner import ProjectScanner

from .syntax_checker import SyntaxChecker

from .report_generator import ReportGenerator





class TestingAgent:
    """
    ASEO Testing Agent v1


    Responsible for:

    - Scanning generated project
    - Checking syntax
    - Creating quality report

    """



    def __init__(self):


        self.scanner = ProjectScanner()


        self.syntax_checker = SyntaxChecker()


        self.report_generator = ReportGenerator()



        self.agent_info = {


            "name":

                "Testing Agent",


            "version":

                "1.0"

        }






    def run(
        self,
        project_path="generated_project"
    ):


        start_time = time.time()



        try:


            files = self.scanner.scan(
                project_path
            )



            results = []



            for file in files:


                result = self.syntax_checker.check(
                    file
                )


                results.append(
                    result
                )





            report = self.report_generator.generate(
                results
            )



            report["agent_info"] = self.agent_info



            report["processing_time"] = round(

                time.time() - start_time,

                3

            )



            return report





        except Exception as error:


            return {


                "status":

                    "failed",


                "agent_info":

                    self.agent_info,


                "error":

                    str(error)

            }