class EnvironmentManager:
    """
    ASEO Environment Manager v15
    """



    def create_environment(
        self,
        project_name
    ):


        return {

            "project":
                project_name,


            "environment_ready":
                True,


            "variables":
            [

                "DATABASE_URL",

                "SECRET_KEY",

                "ENVIRONMENT"

            ]

        }