from ai_engine.software_factory import (
    SoftwareFactory
)

from ai_engine.git_manager import (
    RepositoryManager,
    CommitManager,
    VersionManager
)

from ai_engine.deployment import (
    DeploymentEngine
)



class AutonomousSoftwareFactory:
    """
    ASEO Autonomous Software Factory Master Engine v15
    """



    def __init__(
        self
    ):


        self.factory = SoftwareFactory()


        self.repository = RepositoryManager()


        self.commit = CommitManager()


        self.version = VersionManager()


        self.deployment = DeploymentEngine()





    def build_and_deploy(
        self,
        requirement
    ):


        # 1 - Build software

        software = self.factory.create_software(

            requirement

        )



        project = software["project"]





        # 2 - Git initialization

        repository = self.repository.initialize(

            project

        )



        commit = self.commit.create_commit(

            "Initial commit"

        )



        version = self.version.create_version()




        # 3 - Deployment preparation

        deployment = self.deployment.prepare_deployment(

            project

        )





        return {


            "version":

                "15.0",



            "status":

                "production_ready",



            "project":

                project,



            "architecture":

                software["architecture"],



            "framework":

                software["framework"],



            "database":

                software["database"],



            "files_generated":

                software["files_generated"],



            "tests_generated":

                software["tests_generated"],



            "quality":

                software["quality"],



            "repository":

                repository["repository_created"],



            "commit":

                commit["commit"],



            "version_tag":

                version["version"],



            "deployment":

                deployment["deployment_status"]

        }