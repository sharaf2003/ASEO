from pathlib import Path

from ai_engine.core.base_agent import BaseAgent

from .pipeline import DocumentPipeline





class DocumentAgent(BaseAgent):
    """
    ASEO Document Understanding Agent v2.0

    Reads project requirements from files
    or direct text input.
    """



    def __init__(self):

        super().__init__(

            name="Document Understanding Agent",

            description=
            "Reads and understands project documents or text requirements"

        )


        self.pipeline = DocumentPipeline()





    def execute(
        self,
        task
    ):


        # ==========================
        # File Input
        # ==========================


        file_path = task.get(

            "file"

        )



        if file_path:


            path = Path(file_path)



            if path.exists():


                result = self.pipeline.process(

                    str(path)

                )


                return {


                    "status":

                        "success",


                    "source":

                        "file",


                    "result":

                        result

                }






        # ==========================
        # Text Input
        # ==========================


        text = task.get(

            "text"

        )



        if text:


            return {


                "status":

                    "success",


                "source":

                    "text",


                "content":

                    text

            }







        # ==========================
        # No Input
        # ==========================


        return {


            "status":

                "success",



            "source":

                "memory_context",



            "message":

                "No document provided. Requirements will be generated from project context."

        }