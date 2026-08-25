import os
import json
from datetime import datetime



class ProjectMemoryManager:
    """
    ASEO Project Memory Manager v1

    Isolated memory for each project.
    """



    def __init__(self):

        self.storage_path = "project_memory_storage"


        os.makedirs(
            self.storage_path,
            exist_ok=True
        )

    
    def create_project(
        self,
        project_name
    ):

        project_id = (
            project_name
            .lower()
            .replace(" ", "_")
        )


        return self.create_project_with_id(
            project_id,
            project_name
        )



    def create_project_with_id(
        self,
        project_id,
        project_name
    ):

        project_folder = os.path.join(
            self.storage_path,
            project_id
        )


        os.makedirs(
            project_folder,
            exist_ok=True
        )



        metadata = {

            "project_id": project_id,

            "name": project_name,

            "created_at": datetime.now().isoformat(),

            "status": "active"

        }



        self._write(
            project_folder,
            "metadata.json",
            metadata
        )


        self._write(
            project_folder,
            "documents.json",
            []
        )


        self._write(
            project_folder,
            "requirements.json",
            []
        )


        self._write(
            project_folder,
            "plans.json",
            []
        )


        self._write(
            project_folder,
            "knowledge_graph.json",
            {}
        )


        return metadata





    def save(
        self,
        project_id,
        memory_type,
        data
    ):


        folder = os.path.join(
            self.storage_path,
            project_id
        )


        os.makedirs(
            folder,
            exist_ok=True
        )


        self._write(
            folder,
            f"{memory_type}.json",
            data
        )





    def load(
        self,
        project_id,
        memory_type
    ):


        file_path = os.path.join(

            self.storage_path,

            project_id,

            f"{memory_type}.json"

        )


        if not os.path.exists(file_path):

            return None



        with open(

            file_path,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)





    def _write(
        self,
        folder,
        filename,
        data
    ):


        with open(

            os.path.join(
                folder,
                filename
            ),

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                data,

                file,

                indent=4,

                ensure_ascii=False

            )