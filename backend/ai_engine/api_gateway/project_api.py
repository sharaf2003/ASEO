from fastapi import APIRouter



router = APIRouter()



projects = []





@router.post("/create")
def create_project(
    name: str
):


    project = {


        "project":

            name,


        "status":

            "created"

    }


    projects.append(project)



    return project






@router.get("/all")
def get_projects():


    return {


        "projects":

            projects

    }