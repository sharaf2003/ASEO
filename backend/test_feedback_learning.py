from app.database.connection import SessionLocal
from app.intelligence.learning.learning_engine import LearningEngine
from app.intelligence.feedback.feedback_result import FeedbackResult
from sqlalchemy import text



def run_test():

    print("\n==============================")
    print("ADAPTIVE FEEDBACK LEARNING TEST")
    print("==============================")


    db = SessionLocal()


    learning_engine = LearningEngine(
        db=db
    )


    agent_result = {

        "architecture": {

            "backend": {

                "technology": "Firebase"

            },

            "database": {

                "technology": "Firebase Firestore"

            },

            "frontend": {

                "technology": "Flutter"

            },

            "deployment": {

                "technology": "Firebase"

            }

        }

    }



    print("\nBEFORE UPDATE")



    memory_before = db.execute(

        text(
            """
            SELECT
                id,
                success_score,
                confidence,
                adaptive_decision_score,
                usage_count
            FROM decision_memory
            ORDER BY id DESC
            LIMIT 1
            """
        )

    )


    for row in memory_before:

        print(row)



    feedback = FeedbackResult(

        agent="ArchitectAgent",

        score=1.0,

        confidence=1.0,

        issues=[],

        suggestions=[]

    )



    result = learning_engine.learn(

        feedback,

        agent_result

    )



    print("\nLEARNING RESULT")

    print(result)



    print("\nAFTER UPDATE")



    memory_after = db.execute(

        text(
            """
            SELECT
                id,
                success_score,
                confidence,
                adaptive_decision_score,
                usage_count
            FROM decision_memory
            ORDER BY id DESC
            LIMIT 1
            """
        )

    )


    for row in memory_after:

        print(row)



    db.close()



if __name__ == "__main__":

    run_test()