class KnowledgeAnalyzer:
    """
    ASEO Knowledge Analysis Engine v14
    """



    def __init__(
        self,
        graph
    ):

        self.graph = graph





    def find_related(
        self,
        name
    ):


        results = []



        for edge in self.graph.edges:


            if edge["source"] == name:

                results.append(edge)



            elif edge["target"] == name:

                results.append(edge)



        return results