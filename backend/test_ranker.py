from app.database.session import SessionLocal

from app.intelligence.knowledge_retriever import KnowledgeRetriever

from app.intelligence.pattern_ranker import PatternRanker



db = SessionLocal()



retriever = KnowledgeRetriever(

    db=db

)


ranker = PatternRanker()



patterns = retriever.retrieve(

    layer="backend"

)



results = ranker.rank(

    patterns,

    {

        "layer": "backend"

    }

)



for item in results:

    pattern = item["pattern"]


    print("\n")

    print("Name:", pattern["name"])

    print("Category:", pattern["category"])

    print("Score:", item["score"])

    print("Reason:", item["reason"])

    print("Context:", pattern["context"])