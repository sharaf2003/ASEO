from ai_engine.knowledge_graph import CompanyBrain



brain = CompanyBrain()



result = brain.learn_project(

    {

        "requirement":
        "Build ecommerce platform",

        "framework":
        "FastAPI",

        "architecture":
        "Layered",

        "score":
        100

    }

)



search = brain.search_experience(

    "FastAPI"

)



print({

    "updated":
        result,

    "search":
        search,

    "knowledge":
        brain.knowledge()

})