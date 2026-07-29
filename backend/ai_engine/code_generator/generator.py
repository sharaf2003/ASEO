from .file_builder import (
    FileBuilder
)



class CodeGenerator:
    """
    ASEO Code Generation Engine v15
    """



    def __init__(
        self
    ):


        self.builder = FileBuilder()





    def generate(
        self,
        blueprint
    ):


        project_name = (

            blueprint
            .get(
                "project",
                "generated_project"
            )

        )



        files = []



        main_content = """

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():

    return {
        "message":
        "ASEO Generated API"
    }

"""



        files.append(

            self.builder.create_file(

                f"{project_name}/main.py",

                main_content

            )

        )





        database_content = """

DATABASE = "PostgreSQL"


def connect():

    return True

"""



        files.append(

            self.builder.create_file(

                f"{project_name}/database.py",

                database_content

            )

        )





        modules = blueprint.get(

            "modules",

            []

        )



        for module in modules:


            route_content = f"""

from fastapi import APIRouter


router = APIRouter()


@router.get("/{module}")
def get_{module}():

    return {{

        "module":
        "{module}"

    }}

"""



            files.append(

                self.builder.create_file(

                    f"{project_name}/routes/{module}.py",

                    route_content

                )

            )



        return {


            "project":

                project_name,


            "files":

                files,


            "generated":

                True

        }