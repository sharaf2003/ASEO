from ai_engine.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeNode,
    KnowledgeAnalyzer
)



graph = KnowledgeGraph()



project = KnowledgeNode(

    "Ecommerce Backend",

    "project"

)



framework = KnowledgeNode(

    "FastAPI",

    "framework"

)



database = KnowledgeNode(

    "PostgreSQL",

    "database"

)



graph.add_node(project)

graph.add_node(framework)

graph.add_node(database)



graph.connect(

    "Ecommerce Backend",

    "uses",

    "FastAPI"

)



graph.connect(

    "FastAPI",

    "database",

    "PostgreSQL"

)



analyzer = KnowledgeAnalyzer(

    graph

)



print(

    graph.all()

)



print(

    analyzer.find_related(

        "FastAPI"

    )

)