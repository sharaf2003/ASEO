from ai_engine.learning import LearningEngine


def test_learning_engine():

    learning = LearningEngine()


    result = learning.learn(

        "Ecommerce Backend",

        {
            "framework": "FastAPI",
            "database": "PostgreSQL"
        },

        {
            "files": 10,
            "tests": "passed"
        },

        True,

        98

    )


    assert result is not None

    history = learning.history()

    assert history is not None