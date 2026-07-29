from ai_engine.software_factory import (
    AutonomousSoftwarePipeline
)



factory = AutonomousSoftwarePipeline()



result = factory.build(

    "Build ecommerce platform"

)



print(result)