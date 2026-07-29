from .json_store import JsonStore




class PersistentMemory:
    """
    ASEO Persistent Intelligence Memory v14
    """



    def __init__(self):


        self.store = JsonStore(

            "ai_engine/storage/data/memory.json"

        )





    def remember(
        self,
        item
    ):


        memories = self.store.load()



        memories.append(

            item

        )


        self.store.save(

            memories

        )


        return item





    def recall_all(self):


        return self.store.load()