from app.database.connection import SessionLocal

from app.intelligence.self_improvement.evolution_learning_engine import (
    EvolutionLearningEngine
)

from app.intelligence.self_improvement.evolution_feedback import (
    EvolutionFeedback
)


db = SessionLocal()


engine = EvolutionLearningEngine(
    db
)


print("==============================")
print("BEFORE FAILURE FEEDBACK")
print("==============================")


before = engine.analyze_recommendation(
    "Add Cloud Functions"
)


print(before)



print("==============================")
print("ADDING FAILURE")
print("==============================")


feedback = EvolutionFeedback(

    architecture="Firebase",

    recommendation="Add Cloud Functions",

    success=False

)


engine.record_feedback(
    feedback
)



print("==============================")
print("AFTER FAILURE FEEDBACK")
print("==============================")


after = engine.analyze_recommendation(
    "Add Cloud Functions"
)


print(after)



db.close()