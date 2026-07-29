from ai_engine.learning import (
    LearningEngine
)



learning = LearningEngine()



result = learning.learn(

    "Ecommerce Backend",

    {
        "framework":
            "FastAPI",

        "database":
            "PostgreSQL"
    },


    {
        "files":
            10,

        "tests":
            "passed"
    },


    True,

    98

)



print(result)



print(

    learning.history()

)