from app.database.connection import SessionLocal
from app.intelligence.learning.learning_engine import LearningEngine
from app.intelligence.feedback.feedback_result import FeedbackResult
from sqlalchemy import text



def run_test():

    print("\n==============================")
    print("FAILURE FEEDBACK LEARNING TEST")
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



    print("\nBEFORE FAILURE UPDATE")



    before = db.execute(

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


    for row in before:

        print(row)



    feedback = FeedbackResult(

        agent="ArchitectAgent",

        score=0.3,

        confidence=0.3,

        issues=[
            "Architecture execution failed"
        ],

        suggestions=[
            "Improve pattern selection"
        ]

    )



    result = learning_engine.learn(

        feedback,

        agent_result

    )



    print("\nLEARNING RESULT")

    print(result)



    print("\nAFTER FAILURE UPDATE")



    after = db.execute(

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


    for row in after:

        print(row)



    db.close()



if __name__ == "__main__":

    run_test()