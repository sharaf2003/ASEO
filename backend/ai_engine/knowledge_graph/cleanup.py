class KnowledgeCleanup:
    """
    ASEO Knowledge Graph Cleanup Engine v14.1.3
    """



    def __init__(
        self,
        graph
    ):

        self.graph = graph





    def cleanup_nodes(self):

        unique_nodes = {}



        for node in self.graph.nodes:


            key = (

                node.name.lower(),

                node.node_type.lower()

            )



            if key not in unique_nodes:


                unique_nodes[key] = node



            else:


                existing = unique_nodes[key]


                existing.metadata = self.merge_metadata(

                    existing.metadata,

                    node.metadata

                )



        self.graph.nodes = list(

            unique_nodes.values()

        )


        return self.graph.all()





    def merge_metadata(
        self,
        old,
        new
    ):


        old = old or {}

        new = new or {}



        result = old.copy()



        for key, value in new.items():


            if key == "score":


                result[key] = max(

                    result.get(

                        key,

                        0

                    ),

                    value

                )


            else:


                result[key] = value



        return result