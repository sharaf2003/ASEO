from ai_engine.architect import (
    ArchitectAgent
)

from ai_engine.code_generator import (
    CodeGenerator
)

from ai_engine.project_manager import (
    ProjectFileManager
)

from ai_engine.test_generator import (
    TestGenerator
)

from ai_engine.quality_engine import (
    TestRunner,
    QualityValidator
)



class SoftwareFactory:
    """
    ASEO Autonomous Software Factory v15

    Complete Production Pipeline
    """



    def __init__(
        self
    ):


        self.architect = ArchitectAgent()


        self.generator = CodeGenerator()


        self.project_manager = ProjectFileManager()


        self.test_generator = TestGenerator()


        self.validator = QualityValidator(

            TestRunner()

        )





    def create_software(
        self,
        requirement
    ):


        # 1 - Architecture

        blueprint = self.architect.analyze(

            requirement

        )



        project_name = "ecommerce_api"



        blueprint["project"] = project_name





        # 2 - Create project structure

        project = self.project_manager.create_project(

            project_name

        )





        # 3 - Generate code

        code = self.generator.generate(

            blueprint

        )





        # 4 - Generate tests

        tests = self.test_generator.generate(

            project_name,

            blueprint["modules"]

        )





        # 5 - Quality validation

        quality = self.validator.validate(

            tests["tests"]

        )





        return {


            "version":

                "15.0",



            "status":

                "software_created",



            "project":

                project_name,



            "architecture":

                blueprint["architecture"],



            "framework":

                blueprint["framework"],



            "database":

                blueprint["database"],



            "files_generated":

                len(
                    code["files"]
                ),



            "tests_generated":

                len(
                    tests["tests"]
                ),



            "quality":

                quality

        }