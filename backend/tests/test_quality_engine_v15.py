from ai_engine.quality_engine import (
    TestRunner,
    QualityValidator
)



runner = TestRunner()



validator = QualityValidator(

    runner

)



result = validator.validate(

    [

        "test_main.py",

        "test_users.py",

        "test_products.py",

        "test_orders.py"

    ]

)



print(result)