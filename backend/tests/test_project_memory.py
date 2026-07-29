from ai_engine.memory.project_memory import ProjectMemoryManager



print("===================")
print("PROJECT MEMORY")
print("===================")



memory = ProjectMemoryManager()



project = memory.create_project(

    "Clinic Management System"

)



print(project)



memory.save(

    project["project_id"],

    "documents",

    [

        {

        "file":"requirements.txt"

        }

    ]

)



print(

    memory.load(

        project["project_id"],

        "documents"

    )

)