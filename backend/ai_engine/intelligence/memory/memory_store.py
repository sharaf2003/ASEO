class MemoryStore:
    """
    ASEO Memory Storage v13

    Intelligent memory retrieval
    using keyword matching.
    """



    def __init__(self):

        self.items = []





    def add(
        self,
        item
    ):


        self.items.append(

            item

        )





    def all(self):


        return [

            item.to_dict()

            for item in self.items

        ]





    def search(
        self,
        keyword
    ):


        keywords = keyword.lower().split()



        results = []



        for item in self.items:



            text = (

                item.key

                +

                " "

                +

                item.value

            ).lower()




            matches = 0



            for word in keywords:



                if word in text:

                    matches += 1





            if matches > 0:



                results.append(

                    item.to_dict()

                )





        return results