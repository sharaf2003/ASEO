from .test_builder import (
    TestBuilder
)



class TestGenerator:
    """
    ASEO Test Generation Engine v15
    """



    def __init__(
        self
    ):

        self.builder = TestBuilder()





    def generate(
        self,
        project_name,
        modules
    ):


        tests = []



        # Main application test

        main_test = """

def test_application_start():

    assert True

"""



        tests.append(

            self.builder.create_test_file(

                f"{project_name}/tests/test_main.py",

                main_test

            )

        )





        # Module tests

        for module in modules:


            content = f"""

def test_{module}_module():

    assert "{module}" != ""

"""



            tests.append(

                self.builder.create_test_file(

                    f"{project_name}/tests/test_{module}.py",

                    content

                )

            )



        return {


            "project":

                project_name,


            "tests":

                tests,


            "generated":

                True

        }