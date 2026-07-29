from ai_engine.agents.testing_agent.agent import TestingAgent

from ai_engine.agents.self_healing_agent.agent import SelfHealingAgent



testing_agent = TestingAgent()


healing_agent = SelfHealingAgent()





# الحصول على تقرير حقيقي

testing_report = testing_agent.run()



result = healing_agent.run(

    testing_report,

    testing_agent

)



print("===================")
print("SELF HEALING AGENT")
print("===================")


print(result)