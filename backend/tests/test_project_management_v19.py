from ai_engine.project_management import (
    ProjectManager
)



manager = ProjectManager()



project = manager.create_project(

    "Ecommerce Platform",

    "Client A"

)



manager.assign_team(

    project["id"],

    [

        "backend_engineer",

        "qa_engineer",

        "devops_engineer"

    ]

)



result = manager.update_project(

    project["id"],

    "production",

    100

)



print(result)