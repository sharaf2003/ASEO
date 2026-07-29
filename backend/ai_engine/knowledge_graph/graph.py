from .node import KnowledgeNode



class KnowledgeGraph:
    """
    ASEO Knowledge Graph Engine v14
    """



    def __init__(self):

        self.nodes = []

        self.edges = []





    def add_node(
        self,
        node
    ):


        self.nodes.append(

            node

        )


        return node.to_dict()





    def connect(
        self,
        source,
        relation,
        target
    ):


        self.edges.append(

            {

                "source":
                    source,

                "relation":
                    relation,

                "target":
                    target

            }

        )





    def all(self):

        return {

            "nodes":

                [

                    node.to_dict()

                    for node

                    in self.nodes

                ],


            "edges":

                self.edges

        }