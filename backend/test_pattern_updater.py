from app.database.connection import SessionLocal

from app.repositories.knowledge_repository import KnowledgeRepository

from app.intelligence.self_improvement.pattern_updater import PatternUpdater



def main():


    db = SessionLocal()


    try:

        repository = KnowledgeRepository(db)


        updater = PatternUpdater(

            repository

        )


        result = updater.apply_failure_penalty(

            pattern_id=1,

            penalty_score=0.1

        )


        print(result)


    finally:

        db.close()



if __name__ == "__main__":

    main()