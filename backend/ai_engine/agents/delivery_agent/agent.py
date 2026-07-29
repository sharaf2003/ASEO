import time

from .package_builder import PackageBuilder
from .delivery_report import DeliveryReportGenerator





class DeliveryAgent:
    """
    ASEO Delivery Agent v2.0

    Creates final project packages,
    generates delivery reports
    and validates final delivery.
    """



    def __init__(self):


        self.builder = PackageBuilder()


        self.report_generator = DeliveryReportGenerator()



        self.agent_info = {


            "name":

                "Delivery Agent",



            "version":

                "2.0"

        }





    def run(
        self,
        project_path="generated_project",
        project_name="ASEO_Project"
    ):


        start = time.time()



        try:


            package = self.builder.build_zip(

                project_path,

                project_name

            )





            report = self.report_generator.generate(

                project_name,

                package

            )





            status = "passed"





            if not package:


                status = "warning"









            return {


                "status":

                    status,



                "agent_info":

                    self.agent_info,



                "delivery":

                    {


                        "package":

                            package,


                        "report":

                            report,


                        "completed":

                            True

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