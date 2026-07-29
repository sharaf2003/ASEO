class MemoryRetriever:
    """
    ASEO Memory Retrieval v16.6
    """



    def search(
        self,
        memories,
        keyword
    ):


        results = []


        keyword = keyword.lower()



        for memory in memories:


            text = str(memory).lower()



            if keyword in text:

                results.append(

                    memory

                )



        return results