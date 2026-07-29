from ai_engine.project_manager import (
    ProjectFileManager
)



manager = ProjectFileManager()



result = manager.create_project(

    "ecommerce_project"

)



print(result)