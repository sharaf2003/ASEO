from collections import deque

from ai_engine.database.models import KnowledgePatternModel



class PatternGraphEngine:
    """
    ASEO Pattern Graph Engine v3

    Knowledge Graph Traversal Engine

    Supports:

    Pattern Retrieval
    +
    Pattern Neighbors
    +
    Bidirectional Graph Traversal
    +
    Relationship Chains
    +
    Knowledge Expansion
    +
    Path Discovery
    +
    Graph Summarization
    """



    def __init__(
        self,
        repository
    ):

        self.repository = repository





    # =====================================
    # Get Pattern Object
    # =====================================

    def get_pattern(
        self,
        db,
        pattern_id
    ):


        return (

            db.query(

                KnowledgePatternModel

            )

            .filter(

                KnowledgePatternModel.id == pattern_id

            )

            .first()

        )







    # =====================================
    # Get Direct Neighbors
    # =====================================

    def neighbors(
        self,
        db,
        pattern_id
    ):


        relations = self.repository.get_pattern_relations(

            db,

            pattern_id

        )


        results = []



        for relation in relations:



            if relation.source_id == pattern_id:


                results.append(

                    {

                        "id":
                            relation.target_id,


                        "direction":
                            "outgoing",


                        "relation":
                            relation.relation_type,


                        "confidence":
                            relation.confidence,


                        "usage_count":
                            relation.usage_count

                    }

                )



            else:



                results.append(

                    {

                        "id":
                            relation.source_id,


                        "direction":
                            "incoming",


                        "relation":
                            relation.relation_type,


                        "confidence":
                            relation.confidence,


                        "usage_count":
                            relation.usage_count

                    }

                )



        return results







    # =====================================
    # Breadth First Search
    # =====================================

    def explore(
        self,
        db,
        start_pattern_id,
        depth=2
    ):


        visited = set()

        seen_edges = set()

        graph = []



        queue = deque()


        queue.append(

            (

                start_pattern_id,

                0

            )

        )





        while queue:



            current_id, level = queue.popleft()



            if current_id in visited:

                continue



            visited.add(
                current_id
            )



            if level >= depth:

                continue





            neighbors = self.neighbors(

                db,

                current_id

            )





            for node in neighbors:



                target_id = node.get(
                    "id"
                )



                edge_key = (

                    min(
                        current_id,
                        target_id
                    ),

                    max(
                        current_id,
                        target_id
                    ),

                    node.get(
                        "relation"
                    )

                )



                if edge_key in seen_edges:

                    continue



                seen_edges.add(
                    edge_key
                )




                graph.append(

                    {

                        "source":

                            current_id,


                        "target":

                            target_id,


                        "relation":

                            node.get(
                                "relation"
                            ),


                        "confidence":

                            node.get(
                                "confidence"
                            ),


                        "direction":

                            node.get(
                                "direction"
                            )

                    }

                )



                queue.append(

                    (

                        target_id,

                        level + 1

                    )

                )




        return graph







    # =====================================
    # Find Path Between Patterns
    # =====================================

    def find_path(
        self,
        db,
        source_id,
        target_id,
        max_depth=5
    ):


        queue = deque()



        queue.append(

            (

                source_id,

                []

            )

        )



        visited = set()





        while queue:



            current, path = queue.popleft()



            if current == target_id:

                return path





            if current in visited:

                continue



            visited.add(
                current
            )




            if len(path) >= max_depth:

                continue





            neighbors = self.neighbors(

                db,

                current

            )





            for node in neighbors:



                next_id = node.get(
                    "id"
                )



                queue.append(

                    (

                        next_id,


                        path +

                        [

                            {

                                "from":

                                    current,


                                "to":

                                    next_id,


                                "relation":

                                    node.get(
                                        "relation"
                                    ),


                                "confidence":

                                    node.get(
                                        "confidence"
                                    ),


                                "direction":

                                    node.get(
                                        "direction"
                                    )

                            }

                        ]

                    )

                )




        return None







    # =====================================
    # Expand Knowledge
    # =====================================

    def expand(
        self,
        db,
        pattern_id,
        depth=2
    ):


        pattern = self.get_pattern(

            db,

            pattern_id

        )


        graph = self.explore(

            db,

            pattern_id,

            depth

        )



        return {


            "pattern_id":

                pattern_id,


            "pattern":

                pattern.name
                if pattern
                else None,


            "graph":

                graph,


            "connections":

                len(
                    graph
                )

        }



    # =====================================
    # Get Pattern
    # =====================================

    def get_pattern(
        self,
        db,
        pattern_id
    ):


        patterns = self.repository.get_all_patterns(

            db

        )


        for pattern in patterns:


            if pattern.id == pattern_id:

                return pattern



        return None



    # =====================================
    # Knowledge Summary
    # =====================================

    def summarize(
        self,
        db,
        pattern_id
    ):


        pattern = self.get_pattern(

            db,

            pattern_id

        )


        related = self.neighbors(

            db,

            pattern_id

        )



        return {


            "pattern_id":

                pattern_id,


            "pattern_name":

                pattern.name
                if pattern
                else None,


            "connections":

                len(
                    related
                ),


            "related_patterns":

                related

        }