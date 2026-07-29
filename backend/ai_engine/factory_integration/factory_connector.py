class FactoryConnector:
    """
    ASEO Factory Connector v17.2

    Connects Autonomous Engine
    with Software Factory
    """



    def __init__(
        self
    ):

        self.components = [

            "project_manager",

            "code_generator",

            "test_generator",

            "quality_engine",

            "git_manager",

            "deployment_engine"

        ]





    def available_components(
        self
    ):

        return self.components