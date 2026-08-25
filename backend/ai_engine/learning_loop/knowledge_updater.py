from datetime import datetime
from uuid import uuid4



class KnowledgeUpdater:
    """
    ASEO Knowledge Updater v21

    Builds structured knowledge:

    Project
        |
        | used_pattern
        |
    Architecture Pattern

    + stores learning quality
    """



    def __init__(self):

        self.nodes = []

        self.edges = []

        self.history = []





    def _add_node(
        self,
        name,
        node_type,
        metadata=None
    ):


        node = {

            "id":
                str(uuid4()),


            "name":
                name,


            "type":
                node_type,


            "metadata":
                metadata
                or {}

        }


        self.nodes.append(node)


        return node





    def _add_edge(
        self,
        source,
        target,
        relation
    ):


        edge = {

            "id":
                str(uuid4()),


            "source":
                source,


            "target":
                target,


            "relation":
                relation

        }


        self.edges.append(edge)


        return edge





    def update(
        self,
        project,
        decision,
        analysis
    ):


        quality = analysis.get(
            "quality",
            0
        )


        success = analysis.get(
            "success",
            False
        )



        # -------------------------
        # Project Node
        # -------------------------

        project_node = self._add_node(

            project,

            "project",

            {

                "quality":
                    quality,

                "success":
                    success

            }

        )





        # -------------------------
        # Pattern / Decision Node
        # -------------------------

        pattern_name = decision.get(

            "action",

            "unknown_decision"

        )


        pattern_node = self._add_node(

            pattern_name,

            "pattern",

            {

                "confidence":
                    decision.get(
                        "confidence",
                        0
                    ),


                "reasoning":
                    decision.get(
                        "reasoning",
                        ""
                    )

            }

        )





        # -------------------------
        # Relationship
        # -------------------------

        self._add_edge(

            project_node["id"],

            pattern_node["id"],

            "used_pattern"

        )





        record = {

            "id":
                str(uuid4()),


            "project":
                project,


            "decision":
                decision,


            "quality":
                quality,


            "success":
                success,


            "created_at":
                datetime.now().isoformat()

        }



        self.history.append(record)



        return record





    def export_graph(self):


        return {

            "nodes":
                self.nodes,


            "edges":
                self.edges

        }