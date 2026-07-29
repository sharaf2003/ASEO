from ai_engine.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeGraphUpdater
)



graph = KnowledgeGraph()



updater = KnowledgeGraphUpdater(

    graph

)



result = updater.update_from_result(

    {

        "requirement":
            "Ecommerce Backend",

        "framework":
            "FastAPI",

        "architecture":
            "Layered",

        "score":
            95

    }

)



print(result)