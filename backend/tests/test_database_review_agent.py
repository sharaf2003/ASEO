from ai_engine.agents.database_review_agent.agent import DatabaseReviewAgent



print("===================")
print("DATABASE REVIEW AGENT")
print("===================")



agent = DatabaseReviewAgent()



result = agent.run(

    "generated_project"

)



print(result)