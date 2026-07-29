from ai_engine.company import (
    AutonomousQADepartment
)



qa = AutonomousQADepartment()



result = qa.review_project(

    [

        {

            "agent":
            "backend_engineer",

            "task":
            "Implement Authentication API",

            "status":
            "completed"

        },


        {

            "agent":
            "database_engineer",

            "task":
            "Design Database",

            "status":
            "completed"

        }

    ]

)



print(result)