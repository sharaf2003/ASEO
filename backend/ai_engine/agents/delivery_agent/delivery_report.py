import json
import os





class DeliveryReportGenerator:
    """
    ASEO Delivery Report Generator v1
    """



    def generate(
        self,
        project_name,
        package_path
    ):


        report = {


            "project":

                project_name,


            "status":

                "ready",


            "package":

                package_path,


            "delivery":

                "completed"

        }



        os.makedirs(

            "deliveries",

            exist_ok=True

        )



        with open(

            "deliveries/delivery_report.json",

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                report,

                file,

                indent=4

            )



        return report