from ai_engine.master_factory import (
    AutonomousSoftwareFactory
)



aseo = AutonomousSoftwareFactory()



result = aseo.build_and_deploy(

    "Build ecommerce platform"

)



print(result)