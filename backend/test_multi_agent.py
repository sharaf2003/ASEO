from app.agents.execution.agent_executor import AgentExecutor
from app.agents.agent_plan import AgentExecutionPlan


# استدعاء الوكلاء حسب مشروعك
from app.agents.planner_agent import PlannerAgent
from app.agents.architect_agent import ArchitectAgent
from app.agents.developer_agent import DeveloperAgent


from app.shared.models.execution import ExecutionContext

from app.database.session import SessionLocal



# =============================================
# Database Connection
# =============================================

db = SessionLocal()



# =============================================
# Execution Context
# =============================================

context = ExecutionContext(

    metadata={

        "request":
        "Build a SaaS platform with FastAPI backend and React frontend"

    }

)



# =============================================
# Initialize Agents With Database
# =============================================

planner = PlannerAgent(

    db=db

)


architect = ArchitectAgent(

    db=db

)


developer = DeveloperAgent(

    db=db

)



# =============================================
# Multi Agent Execution Plan
# =============================================

plan = AgentExecutionPlan(

    agents=[

        planner,

        architect,

        developer

    ],

    execution_order=[

        "PlannerAgent",

        "ArchitectAgent",

        "DeveloperAgent"

    ],

    reasons=[

        "Planning",

        "Architecture",

        "Development"

    ]

)



# =============================================
# Agent Executor
# =============================================

executor = AgentExecutor(

    db=db

)



results = executor.execute(

    plan,

    context

)



# =============================================
# Feedback Results
# =============================================

print("\nFeedback Results:\n")


for key, value in context.metadata.items():

    if "feedback" in key:

        print(key)

        print(value)

        print("----------------")



# =============================================
# Learning Results
# =============================================

print("\nLearning Results:\n")


for key, value in context.metadata.items():

    if "learning" in key:

        print(key)

        print(value)

        print("----------------")

print("\nQuality Results:\n")


for key, value in context.metadata.items():

    if "quality" in key:

        print(key)

        print(value)

        print("----------------")


print("\nOptimization Results:\n")


for key, value in context.metadata.items():

    if "optimization" in key:

        print(key)

        print(value)

        print("----------------")       

# =============================================
# Execution Results
# =============================================

print("\nExecution Results:\n")


for agent, result in results.items():

    print(agent)

    print(result)

    print("----------------")

# Adaptive Ranking Check

print("\nAdaptive Ranking Check:\n")


architecture_result = context.metadata.get(
    "architecture_result",
    {}
)


decisions = architecture_result.get(
    "architecture_decisions",
    []
)


for decision in decisions:

    print({

        "pattern": decision.get("pattern"),

        "score": decision.get("score"),

        "adaptive_decision_score": decision.get(
            "adaptive_decision_score",
            "NOT FOUND"
        )

    })

    print("----------------")


# Close Database

db.close()