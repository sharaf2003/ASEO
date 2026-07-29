from ai_engine.executive_dashboard import (
    DashboardAgent
)



dashboard = DashboardAgent()



result = dashboard.create_dashboard(

    {

        "department":
        "CEO",

        "decision":
        "Scale company"

    },


    {

        "department":
        "CFO",

        "profit_margin":
        60,

        "score":
        95

    },


    {

        "department":
        "CMO",

        "growth":
        "high",

        "score":
        90

    },


    {

        "department":
        "COO",

        "productivity":
        83,

        "score":
        85

    }

)



print(result)