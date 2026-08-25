from ai_engine.memory.knowledge_store import KnowledgeStore



def test_knowledge_store():

    memory = KnowledgeStore()


    memory.store_requirements(
        [
            {
                "actor": "customer",
                "action": "book",
                "object": "appointments"
            }
        ]
    )


    memory.store_graph(
        {
            "nodes": [
                "customer",
                "appointments"
            ]
        }
    )


    result = memory.get_memory()


    assert result is not None