from ai_engine.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeCleanup
)



graph = KnowledgeGraph()



node1 = KnowledgeNode(

    "FastAPI",

    "framework",

    {
        "score":90
    }

)



node2 = KnowledgeNode(

    "FastAPI",

    "framework",

    {
        "score":95
    }

)



node3 = KnowledgeNode(

    "PostgreSQL",

    "database",

    {
        "score":95
    }

)



graph.add_node(node1)

graph.add_node(node2)

graph.add_node(node3)



print(

    "Before:"

)



print(

    graph.all()

)



cleanup = KnowledgeCleanup(

    graph

)



print(

    "After:"

)



print(

    cleanup.cleanup_nodes()

)