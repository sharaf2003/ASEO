from .graph import KnowledgeGraph

from .node import KnowledgeNode

from .updater import KnowledgeGraphUpdater

from .analyzer import KnowledgeAnalyzer



class CompanyBrain:
    """
    ASEO Company Brain v21.6
    """

    def __init__(self):

        self.graph = KnowledgeGraph()

        self.updater = KnowledgeGraphUpdater(
            self.graph
        )

        self.analyzer = KnowledgeAnalyzer(
            self.graph
        )



    def learn_project(
        self,
        result
    ):

        return self.updater.update_from_result(

            result

        )



    def search_experience(
        self,
        name
    ):

        return self.analyzer.find_related(

            name

        )



    def knowledge(self):

        return self.graph.all()