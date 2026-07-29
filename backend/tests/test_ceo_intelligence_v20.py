from ai_engine.ceo_intelligence import (
    CEOAgent
)



ceo = CEOAgent()



result = ceo.analyze_company(

    {

        "quality":

            95,

        "projects":

            5

    }

)



print(result)