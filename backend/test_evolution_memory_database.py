from app.database.connection import SessionLocal

from app.repositories.evolution_memory_repository import (
    EvolutionMemoryRepository
)



db = SessionLocal()



repo = EvolutionMemoryRepository(
    db
)



result = repo.save_feedback(

    "Firebase",

    "Add Cloud Functions",

    True

)



print(

    result.architecture,

    result.recommendation,

    result.success_rate,

    result.confidence

)



db.close()