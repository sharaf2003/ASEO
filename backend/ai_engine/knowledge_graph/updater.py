from .node import KnowledgeNode



class KnowledgeGraphUpdater:
    """
    ASEO Knowledge Graph Auto Updater v15

    Intelligent knowledge accumulation.
    """



    def __init__(
        self,
        graph
    ):

        self.graph = graph





    def update_from_result(
        self,
        result
    ):


        project_name = result.get(

            "requirement",

            "unknown"

        )



        score = result.get(

            "score",

            0

        )



        decision = result.get(

            "decision",

            {}

        )



        action = decision.get(

            "action",

            ""

        )





        existing = self.graph.find_node(

            project_name,

            "project"

        )





        if existing:


            metadata = existing.metadata



            old_count = metadata.get(

                "executions",

                0

            )



            old_score = metadata.get(

                "average_score",

                0

            )



            new_count = old_count + 1



            metadata.update({

                "executions":

                    new_count,


                "last_score":

                    score,


                "average_score":

                    round(

                        (

                            old_score * old_count

                            +

                            score

                        )

                        /

                        new_count,

                        2

                    ),


                "last_decision":

                    action

            })



        else:


            project_node = KnowledgeNode(

                project_name,

                "project",

                {


                    "executions":

                        1,


                    "last_score":

                        score,


                    "average_score":

                        score,


                    "last_decision":

                        action

                }

            )


            self.graph.add_node(

                project_node

            )





        # Add architecture relationship

        if action:


            architecture_node = KnowledgeNode(

                action,

                "architecture"

            )


            self.graph.add_node(

                architecture_node

            )


            self.graph.connect(

                project_name,

                "uses_architecture",

                action

            )





        return self.graph.all()