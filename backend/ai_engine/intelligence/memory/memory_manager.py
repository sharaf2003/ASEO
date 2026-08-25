from .memory_item import MemoryItem

from ai_engine.database import (
    SessionLocal,
    DatabaseRepository
)




class MemoryManager:
    """
    ASEO Persistent Memory Intelligence v21

    RAM Memory
    +
    PostgreSQL Persistence
    """



    def __init__(self):

        self.repository = DatabaseRepository()





    def remember(
        self,
        key,
        value,
        category="general",
        confidence=1.0
    ):


        item = MemoryItem(

            key,

            value,

            category,

            confidence

        )



        db = SessionLocal()



        try:


            saved = self.repository.save_agent_memory(

                db,

                agent_name=key,

                memory_type=category,

                content={

                    "value":

                        value,


                    "confidence":

                        confidence

                }

            )


            return {

                "key":

                    key,


                "value":

                    value,


                "category":

                    category,


                "confidence":

                    confidence,


                "id":

                    saved.id

            }



        finally:

            db.close()







    def recall(
        self,
        keyword
    ):

        db = SessionLocal()

        try:

            memories = self.repository.get_agent_memories(
                db
            )

            results = []

            keyword_words = set(
                keyword.lower().split()
            )


            for memory in memories:

                content = memory.content or {}

                text = (
                    memory.agent_name
                    + " "
                    + str(
                        content.get(
                            "value",
                            ""
                        )
                    )
                ).lower()


                text_words = set(
                    text.split()
                )


                # partial semantic match
                if keyword_words.intersection(text_words):

                    results.append(
                        {
                            "key": memory.agent_name,

                            "value": content.get(
                                "value"
                            ),

                            "category": memory.memory_type,

                            "confidence": content.get(
                                "confidence",
                                0
                            )
                        }
                    )


            return results


        finally:
            db.close()





    def memories(self):


        db = SessionLocal()



        try:


            records = self.repository.get_agent_memories(

                db

            )


            result = []



            for memory in records:


                content = memory.content or {}



                result.append(

                    {

                        "key":

                            memory.agent_name,


                        "value":

                            content.get(
                                "value"
                            ),


                        "category":

                            memory.memory_type,


                        "confidence":

                            content.get(
                                "confidence",
                                0
                            )

                    }

                )



            return result



        finally:

            db.close()