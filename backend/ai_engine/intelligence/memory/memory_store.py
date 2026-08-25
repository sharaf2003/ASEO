class MemoryStore:
    """
    ASEO Memory Storage v14

    Intelligent memory storage with:

    - Duplicate detection
    - Memory reinforcement
    - Confidence evolution
    """



    def __init__(self):

        self.items = []






    def add(
        self,
        item
    ):

        existing = self.find_exact(

            item.key,

            item.value,

            item.category

        )


        # Existing memory found

        if existing:


            existing.reinforce()


            return existing



        # New memory

        self.items.append(

            item

        )


        return item






    def find_exact(
        self,
        key,
        value,
        category
    ):


        for item in self.items:


            if (

                item.key.lower().strip()
                ==
                key.lower().strip()

                and

                item.value.lower().strip()
                ==
                value.lower().strip()

                and

                item.category
                ==
                category

            ):

                return item



        return None






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


                item.reinforce()


                results.append(

                    item.to_dict()

                )



        return results