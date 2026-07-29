from ai_engine.code_generator import (
    CodeGenerator
)



generator = CodeGenerator()



blueprint = {

    "project":
        "ecommerce_api",


    "framework":
        "FastAPI",


    "database":
        "PostgreSQL",


    "modules":
    [
        "users",
        "products",
        "orders"
    ]

}



result = generator.generate(

    blueprint

)



print(result)