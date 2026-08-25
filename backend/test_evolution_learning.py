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



engine.record_feedback(

    EvolutionFeedback(

        architecture="Firebase",

        recommendation="Add Cloud Functions",

        success=True,

        impact_score=0.9

    )

)



engine.record_feedback(

    EvolutionFeedback(

        architecture="Firebase",

        recommendation="Add Cloud Functions",

        success=True,

        impact_score=0.8

    )

)



result = engine.analyze_recommendation(
    "Add Cloud Functions"
)



print(result)



db.close()