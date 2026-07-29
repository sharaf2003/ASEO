from ai_engine.test_generator import (
    TestGenerator
)



generator = TestGenerator()



result = generator.generate(

    "ecommerce_api",

    [

        "users",

        "products",

        "orders"

    ]

)



print(result)