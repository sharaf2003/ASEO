from ai_engine.testing_pipeline import (
    AutonomousTestingPipeline
)



pipeline = AutonomousTestingPipeline()



result = pipeline.test(

    "ecommerce_api"

)



print(result)