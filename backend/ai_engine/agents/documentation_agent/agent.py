import os
import time

from .document_generator import DocumentGenerator





class DocumentationAgent:
    """
    ASEO Documentation Agent v2.0

    Generates project documentation,
    architecture docs and API documentation.
    """



    def __init__(self):


        self.generator = DocumentGenerator()



        self.agent_info = {


            "name":

                "Documentation Agent",



            "version":

                "2.0"

        }





    def run(
        self,
        project_path="generated_project",
        project_name="ASEO Project"
    ):


        start = time.time()



        try:


            docs_path = os.path.join(

                project_path,

                "docs"

            )


            os.makedirs(

                docs_path,

                exist_ok=True

            )





            files = {


                "README.md":

                    self.generator.generate_readme(

                        project_name

                    ),



                "docs/architecture.md":

                    self.generator.generate_architecture(),



                "docs/api.md":

                    self.generator.generate_api_docs()

            }





            created_files = []





            for path, content in files.items():


                full_path = os.path.join(

                    project_path,

                    path

                )



                directory = os.path.dirname(

                    full_path

                )



                os.makedirs(

                    directory,

                    exist_ok=True

                )





                with open(

                    full_path,

                    "w",

                    encoding="utf-8"

                ) as file:


                    file.write(content)



                created_files.append(

                    full_path

                )







            return {


                "status":

                    "passed",



                "agent_info":

                    self.agent_info,



                "documentation":

                    {


                        "files_created":

                            created_files,


                        "files_count":

                            len(created_files)

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