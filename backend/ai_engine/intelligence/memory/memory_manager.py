from .memory_item import MemoryItem

from .memory_store import MemoryStore




class MemoryManager:
    """
    ASEO Memory Intelligence Manager v13
    """



    def __init__(self):

        self.store = MemoryStore()




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


        self.store.add(

            item

        )



        return item.to_dict()





    def recall(
        self,
        keyword
    ):


        return self.store.search(

            keyword

        )




    def memories(self):


        return self.store.all()