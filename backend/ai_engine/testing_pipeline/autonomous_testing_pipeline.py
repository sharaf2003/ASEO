from .test_connector import (
    TestConnector
)





class AutonomousTestingPipeline:
    """
    ASEO Autonomous Testing Pipeline v17.4
    """



    def __init__(
        self
    ):


        self.connector = TestConnector()





    def test(
        self,
        project
    ):


        generated_tests = self.connector.generate_tests(

            project

        )



        quality = self.connector.run_tests(

            generated_tests["tests"]

        )



        return {


            "version":

                "17.4",



            "status":

                "tested",



            "project":

                project,



            "tests":

                generated_tests,



            "quality":

                quality

        }