from ai_engine.agents.database_review_agent.agent import DatabaseReviewAgent



print("===================")
print("DATABASE REVIEW ASEO v11")
print("===================")



agent = DatabaseReviewAgent()



result = agent.run(

    "app"

)



print(result)