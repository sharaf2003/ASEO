from ai_engine.memory.knowledge_store import KnowledgeStore



memory = KnowledgeStore()



memory.store_requirements(

    [

        {
            "actor":"customer",
            "action":"book",
            "object":"appointments"
        }

    ]

)



memory.store_graph(

    {

        "nodes":[
            "customer",
            "appointments"
        ]

    }

)



print(
    memory.get_memory()
)