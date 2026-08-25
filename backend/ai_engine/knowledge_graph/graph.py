from .node import KnowledgeNode



class KnowledgeGraph:
    """
    ASEO Knowledge Graph Engine v15

    Supports:
    - Node deduplication
    - Knowledge accumulation
    - Relationship memory
    """


    def __init__(self):

        self.nodes = []

        self.edges = []





    def find_node(
        self,
        name,
        node_type=None
    ):

        for node in self.nodes:

            if node.name == name:

                if node_type is None or node.node_type == node_type:

                    return node


        return None





    def add_node(
        self,
        node
    ):


        existing = self.find_node(

            node.name,

            node.node_type

        )


        if existing:


            existing.metadata.update(

                node.metadata

            )


            return existing.to_dict()



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


        edge = {

            "source":
                source,

            "relation":
                relation,

            "target":
                target

        }



        if edge not in self.edges:

            self.edges.append(

                edge

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