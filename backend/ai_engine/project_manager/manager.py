import os

from .structure import (
    ProjectStructure
)

from .workspace import (
    WorkspaceManager
)



class ProjectFileManager:
    """
    ASEO Project File System Manager v15
    """



    def __init__(
        self
    ):


        self.structure = ProjectStructure()


        self.workspace = WorkspaceManager()





    def create_project(
        self,
        project_name
    ):


        created = []


        base_path = project_name





        for directory in self.structure.directories:


            path = os.path.join(

                base_path,

                directory

            )


            self.workspace.create_directory(

                path

            )


            created.append(

                path

            )





        for file in self.structure.files:


            path = os.path.join(

                base_path,

                file

            )


            self.workspace.create_file(

                path

            )


            created.append(

                path

            )





        return {


            "project":

                project_name,


            "created_items":

                created,


            "ready":

                True

        }