from ai_engine.learning_loop import (
    LearningLoop
)



loop = LearningLoop()



result = loop.process(

    project="Ecommerce Platform",

    prompt="Build ecommerce backend",

    improved_prompt="Build scalable ecommerce backend",

    agents=[

        "backend_engineer",

        "database_engineer",

        "security_engineer"

    ],

    result={

        "decision":

            "FastAPI + PostgreSQL + Layered",

        "quality":

            100

    },

    old_score=90,

    new_score=99

)



print(result)