import os
import json



class MemorySearcher:
    """
    ASEO Memory Searcher v1

    Searches previous projects.
    """



    def __init__(self):

        self.storage_path = "project_memory_storage"





    def search(
        self,
        keyword
    ):


        results = []



        if not os.path.exists(
            self.storage_path
        ):

            return results




        projects = os.listdir(

            self.storage_path

        )



        for project_id in projects:


            project_path = os.path.join(

                self.storage_path,

                project_id

            )



            metadata_file = os.path.join(

                project_path,

                "metadata.json"

            )



            if not os.path.exists(
                metadata_file
            ):

                continue




            with open(

                metadata_file,

                "r",

                encoding="utf-8"

            ) as file:


                metadata = json.load(file)





            if keyword.lower() in metadata["name"].lower():


                results.append(

                    metadata

                )



        return results