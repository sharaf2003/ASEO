from ai_engine.agent_collaboration import CollaborationManager



manager = CollaborationManager()



result = manager.collaborate(

    "Build authentication system",

    [

        "backend_engineer",

        "database_engineer",

        "security_engineer"

    ]

)



print(result)