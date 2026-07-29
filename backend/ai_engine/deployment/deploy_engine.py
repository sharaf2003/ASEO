from .docker_manager import (
    DockerManager
)

from .environment import (
    EnvironmentManager
)



class DeploymentEngine:
    """
    ASEO Deployment Intelligence v15
    """



    def __init__(
        self
    ):


        self.docker = DockerManager()


        self.environment = EnvironmentManager()





    def prepare_deployment(
        self,
        project_name
    ):


        docker = self.docker.create_dockerfile(

            project_name

        )


        environment = self.environment.create_environment(

            project_name

        )



        return {


            "project":
                project_name,


            "docker":
                docker,


            "environment":
                environment,


            "deployment_status":
                "ready"

        }