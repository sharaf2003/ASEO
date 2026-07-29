from ai_engine.reporting import (
    FinalReportGenerator
)



generator = FinalReportGenerator()



report = generator.generate(

    "Build ecommerce platform",


    {
        "recommendation":
        {
            "framework":
                "FastAPI",

            "database":
                "PostgreSQL"
        },

        "confidence":
            0.98
    },


    {
        "status":
            "completed"
    },


    {
        "experience":
        {
            "score":
                95
        },


        "evaluation":
        {
            "planning":
            {
                "quality_score":
                    95
            },

            "coding":
            {
                "quality_score":
                    95
            }
        },


        "improvement":
        {
            "old_score":
                75,

            "new_score":
                95,

            "improved":
                True
        }
    },


    {
        "nodes":
        [
            "FastAPI",
            "PostgreSQL"
        ]
    }

)



print(report)