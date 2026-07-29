from ai_engine.storage import (
    PersistentMemory
)

from .knowledge_ranker import (
    KnowledgeRanker
)



class MemoryRetriever:
    """
    ASEO Intelligent Memory Retrieval v14
    """



    def __init__(self):

        self.memory = PersistentMemory()

        self.ranker = KnowledgeRanker()





    def retrieve(
        self,
        query
    ):


        memories = self.memory.recall_all()



        query_words = (

            query.lower()

            .split()

        )



        matches = []



        for item in memories:


            text = str(item).lower()



            score = sum(

                1

                for word in query_words

                if word in text

            )



            if score > 0:

                item["match_score"] = score

                matches.append(item)





        return self.ranker.rank(

            matches

        )