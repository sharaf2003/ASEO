from ai_engine.software_factory import (
    SoftwareFactoryEngine
)



factory = SoftwareFactoryEngine()



result = factory.create_project(

    "Build ecommerce backend"

)



print(result)