from ai_engine.code_pipeline import (
    AutonomousCodeGenerationPipeline
)



pipeline = AutonomousCodeGenerationPipeline()



result = pipeline.generate(

    {

        "project":
            "ecommerce_api",


        "architecture":
            "Layered",


        "framework":
            "FastAPI",


        "database":
            "PostgreSQL"

    }

)



print(result)