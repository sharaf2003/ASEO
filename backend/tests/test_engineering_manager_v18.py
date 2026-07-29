from ai_engine.company import (
    EngineeringManagerAgent
)



manager = EngineeringManagerAgent()



result = manager.manage(

    {

        "product":
            "Ecommerce Platform",


        "features":
        [

            "User Authentication",

            "Product Management",

            "Order Management",

            "Payment Integration",

            "Admin Dashboard"

        ]

    }

)



print(result)