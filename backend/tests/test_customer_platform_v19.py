from ai_engine.customer_platform import (
    CustomerManager
)



manager = CustomerManager()



customer = manager.create_customer(

    "Startup Company",

    "Professional"

)



workspace = manager.create_workspace(

    customer["id"],

    "Main Workspace"

)



dashboard = manager.customer_dashboard(

    customer["id"]

)



print({

    "customer":
        customer,

    "workspace":
        workspace,

    "dashboard":
        dashboard

})