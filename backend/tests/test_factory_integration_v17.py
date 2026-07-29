from ai_engine.factory_integration import (
    AutonomousSoftwareFactoryEngine
)



engine = AutonomousSoftwareFactoryEngine()



result = engine.build(

    {

        "project":
            "ecommerce_api",


        "architecture":
            "Layered",


        "framework":
            "FastAPI",


        "database":
            "PostgreSQL",


        "modules":
            [

                "authentication",

                "users",

                "products",

                "orders"

            ]

    }

)



print(result)