from ai_engine.customer_portal import (
    AuthManager,
    CustomerPortal
)



auth = AuthManager()



user = auth.register(

    "owner@startup.com",

    "123456",

    "owner",

    "customer_001"

)



login = auth.login(

    "owner@startup.com",

    "123456"

)



portal = CustomerPortal()



dashboard = portal.dashboard(

    user,

    {

        "plan":
        "Professional",

        "status":
        "active"

    },

    [

        "Ecommerce Platform",

        "CRM System"

    ]

)



print({

    "user":
        user,

    "login":
        login,

    "dashboard":
        dashboard

})