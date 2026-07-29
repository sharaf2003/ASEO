from ai_engine.deployment import (
    DeploymentEngine
)



engine = DeploymentEngine()



result = engine.prepare_deployment(

    "ecommerce_api"

)



print(result)