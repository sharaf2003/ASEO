from ai_engine.agents.planning_agent.agent import PlanningAgent


print("===================")
print("PLANNING AGENT v5")
print("===================")


agent = PlanningAgent()


memory_context = {

    "recommendations":
    {
        "backend":"FastAPI",
        "database":"PostgreSQL",
        "architecture":"MVC",
        "authentication":"JWT"
    }

}



result = agent.run(

    memory_context

)



print(result)