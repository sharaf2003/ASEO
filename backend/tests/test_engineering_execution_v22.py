from ai_engine.engineering_execution import EngineeringManager



manager = EngineeringManager()



result = manager.execute(

    [

        {
            "feature":
            "User Authentication"
        },

        {
            "feature":
            "Knowledge Base"
        },

        {
            "feature":
            "Analytics Dashboard"
        }

    ]

)



print(result)