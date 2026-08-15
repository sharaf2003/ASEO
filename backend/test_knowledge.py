from app.database.session import SessionLocal

from app.intelligence.knowledge_retriever import KnowledgeRetriever



db = SessionLocal()


retriever = KnowledgeRetriever(

    db=db

)



result = retriever.recommend_stack()



for layer, patterns in result.items():

    print("\n", layer)

    for item in patterns:

        print(

            item["name"],

            item["success_rate"],

            item["context"]

        )