class RepositoryManager:
    """
    ASEO Repository Manager v22.2
    """

    def create_repository(
        self,
        project
    ):

        return {

            "repository":
                project,

            "branch":
                "main",

            "status":
                "created"

        }