import os
import time

from .docker_generator import DockerGenerator
from .deployment_validator import DeploymentValidator





class DeploymentAgent:
    """
    ASEO Deployment Agent v2.0

    Generates deployment files,
    validates deployment readiness
    and prepares projects for production.
    """



    def __init__(self):


        self.generator = DockerGenerator()


        self.validator = DeploymentValidator()



        self.agent_info = {


            "name":

                "Deployment Agent",



            "version":

                "2.0"

        }





    def run(
        self,
        project_path="generated_project"
    ):


        start = time.time()



        try:


            generated = self.generator.generate(

                project_path

            )



            created_files = []





            for name, content in generated.items():


                file_path = os.path.join(

                    project_path,

                    name

                )



                with open(

                    file_path,

                    "w",

                    encoding="utf-8"

                ) as file:


                    file.write(content)



                created_files.append(

                    file_path

                )





            validation = self.validator.validate(

                project_path

            )





            status = "passed"





            for item in validation:


                if not item.get(
                    "exists",
                    False
                ):


                    status = "warning"









            return {


                "status":

                    status,



                "agent_info":

                    self.agent_info,



                "deployment":

                    {


                        "generated_files":

                            created_files,


                        "validation":

                            validation

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