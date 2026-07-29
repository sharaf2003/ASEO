class RequirementGraphBuilder:
    """
    ASEO Requirement Knowledge Graph v1

    Converts extracted requirements into
    a graph representation.

    Input:

    [
        {
            "actor":"admin",
            "action":"manage",
            "object":"users"
        }
    ]

    Output:

    {
        "nodes":[],
        "edges":[]
    }

    """



    def __init__(self):

        self.nodes = []

        self.edges = []



    # =====================================
    # Build Graph
    # =====================================

    def build(
        self,
        requirements
    ):


        self.nodes = []

        self.edges = []


        for requirement in requirements:


            actor = requirement.get(
                "actor"
            )


            action = requirement.get(
                "action"
            )


            obj = requirement.get(
                "object"
            )



            if actor:


                self.add_node(

                    actor,

                    "actor"

                )



            if obj:


                self.add_node(

                    obj,

                    "entity"

                )



            if actor and obj:


                self.add_edge(

                    actor,

                    action,

                    obj

                )



        return {


            "nodes":
                self.nodes,


            "edges":
                self.edges

        }



    # =====================================
    # Add Node
    # =====================================

    def add_node(
        self,
        name,
        node_type
    ):


        exists = any(

            node["id"] == name

            for node in self.nodes

        )


        if not exists:


            self.nodes.append(

                {

                    "id":
                        name,


                    "type":
                        node_type

                }

            )



    # =====================================
    # Add Edge
    # =====================================

    def add_edge(
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