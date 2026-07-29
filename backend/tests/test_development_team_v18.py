from ai_engine.company import (
    AutonomousDevelopmentTeam
)



team = AutonomousDevelopmentTeam()



result = team.execute_plan(

    [

        {

            "task":
            "Implement User Authentication",

            "assigned_to":
            "backend_engineer"

        },


        {

            "task":
            "Design Product Database",

            "assigned_to":
            "database_engineer"

        },


        {

            "task":
            "Secure Payment System",

            "assigned_to":
            "security_engineer"

        }

    ]

)



print(result)