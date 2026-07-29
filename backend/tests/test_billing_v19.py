from ai_engine.billing import (
    BillingManager
)



billing = BillingManager()



plan = billing.create_plan(

    "Professional",

    199,

    10,

    50

)



subscription = billing.subscribe(

    "customer_001",

    plan["id"]

)



billing.track_usage(

    "customer_001",

    "projects"

)



result = {

    "plan":
        plan,

    "subscription":
        subscription,

    "usage":
        billing.usage["customer_001"]

}



print(result)