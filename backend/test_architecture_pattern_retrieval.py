from app.database.connection import SessionLocal

from app.intelligence.knowledge_retriever import (
    KnowledgeRetriever
)



def main():


    db = SessionLocal()


    try:


        retriever = KnowledgeRetriever(

            db=db

        )


        patterns = (
            retriever
            .retrieve_architecture_patterns(
                request_text=
                "Build a SaaS platform with FastAPI backend and React frontend"
            )
        )


        print("\nArchitecture Patterns Results:\n")


        for pattern in patterns:

            print(pattern)

            print("----------------")



    finally:


        db.close()



if __name__ == "__main__":

    main()