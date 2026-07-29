from .node import KnowledgeNode



class KnowledgeGraphUpdater:
    """
    ASEO Knowledge Graph Auto Updater v14.1
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



        framework = result.get(

            "framework"

        )



        architecture = result.get(

            "architecture"

        )



        decision = result.get(

            "decision",

            {}

        )





        project_node = KnowledgeNode(

            project_name,

            "project",

            {

                "score":

                    result.get(

                        "score",

                        0

                    )

            }

        )



        self.graph.add_node(

            project_node

        )





        if framework:


            framework_node = KnowledgeNode(

                framework,

                "framework"

            )


            self.graph.add_node(

                framework_node

            )


            self.graph.connect(

                project_name,

                "uses",

                framework

            )





        if architecture:


            architecture_node = KnowledgeNode(

                architecture,

                "architecture"

            )


            self.graph.add_node(

                architecture_node

            )


            self.graph.connect(

                project_name,

                "architecture",

                architecture

            )





        return self.graph.all()