class IntelligenceQuery:
    """
    ASEO Intelligence Query v21.6
    """

    def search(
        self,
        data,
        keyword
    ):

        results = []


        for item in data:

            if keyword.lower() in str(item).lower():

                results.append(item)


        return results