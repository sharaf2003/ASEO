from ai_engine.learning_loop import LearningLoop


def test_learning_loop_v14():

    loop = LearningLoop()


    result = loop.process(

        "Ecommerce Backend",

        "Generate backend API",

        "Generate scalable FastAPI backend API with JWT authentication",

        [
            "planning",
            "coding",
            "security"
        ],

        {
            "decision": {
                "framework": "FastAPI",
                "database": "PostgreSQL"
            },

            "files": 10
        },

        75,

        95

    )


    assert result is not None