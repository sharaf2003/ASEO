from ai_engine.llm_router import (
    IntelligenceRouter
)



router = IntelligenceRouter()



results = [

    router.select_model(

        "Design system architecture"

    ),


    router.select_model(

        "Generate FastAPI code"

    ),


    router.select_model(

        "Fix database error"

    ),


    router.select_model(

        "Analyze security issue"

    )

]



for result in results:

    print(result)