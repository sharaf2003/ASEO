from ai_engine.security_governance import GovernanceManager



manager = GovernanceManager()



result = manager.evaluate(

    "owner@startup.com",

    "admin",

    "deploy"

)



print(result)