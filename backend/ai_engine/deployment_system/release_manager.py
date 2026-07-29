from .repository_manager import RepositoryManager

from .build_engine import BuildEngine

from .ci_pipeline import CIPipeline

from .deployment_engine import DeploymentEngine



class ReleaseManager:
    """
    ASEO Autonomous Release Manager v22.2
    """

    def __init__(self):

        self.repository = RepositoryManager()

        self.build = BuildEngine()

        self.ci = CIPipeline()

        self.deploy_engine = DeploymentEngine()



    def release(
        self,
        project
    ):


        repo = self.repository.create_repository(

            project

        )


        build = self.build.build(

            repo

        )


        tests = self.ci.run(

            build

        )


        deployment = self.deploy_engine.deploy(

            build

        )


        return {

            "repository":
                repo,

            "build":
                build,

            "tests":
                tests,

            "deployment":
                deployment,

            "status":
                "live"

        }