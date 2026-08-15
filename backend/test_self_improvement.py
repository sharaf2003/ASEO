from app.database.connection import SessionLocal

from app.repositories.knowledge_repository import KnowledgeRepository

from app.intelligence.self_improvement.self_improvement_engine import (
    SelfImprovementEngine
)



def main():


    db = SessionLocal()


    try:


        repository = KnowledgeRepository(db)


        engine = SelfImprovementEngine(

            repository

        )


        result = engine.process_failure(

            execution_result={

                "success": False

            },


            architecture_decisions=[

                {

                    "id": 1,

                    "pattern": "FastAPI",

                    "layer": "backend"

                }

            ]

        )


        print(result)



    finally:

        db.close()



if __name__ == "__main__":

    main()