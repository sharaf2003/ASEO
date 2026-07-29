from .product_analyzer import ProductAnalyzer

from .feature_generator import FeatureGenerator

from .user_story_generator import UserStoryGenerator

from .roadmap_builder import RoadmapBuilder




class ProductManager:
    """
    ASEO Autonomous Product Manager v21.9
    """

    def __init__(self):

        self.analyzer = ProductAnalyzer()

        self.features = FeatureGenerator()

        self.stories = UserStoryGenerator()

        self.roadmap = RoadmapBuilder()



    def create_product(
        self,
        idea
    ):


        analysis = self.analyzer.analyze(

            idea

        )


        features = self.features.generate(

            analysis

        )


        stories = self.stories.generate(

            features

        )


        roadmap = self.roadmap.build(

            features

        )


        return {

            "analysis":
                analysis,

            "features":
                features,

            "user_stories":
                stories,

            "roadmap":
                roadmap,

            "status":
                "ready_for_development"

        }