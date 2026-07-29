from ai_engine.software_creator import (
    AutonomousSoftwareCreationEngine
)



engine = AutonomousSoftwareCreationEngine()



result = engine.create(

    {

        "architecture":
            "Layered",

        "framework":
            "FastAPI",

        "database":
            "PostgreSQL"

    }

)



print(result)