import os



class DeploymentValidator:
    """
    ASEO Deployment Validator v1
    """



    def validate(
        self,
        project_path
    ):


        required = [

            "Dockerfile",

            "docker-compose.yml",

            "requirements.txt"

        ]



        result = []



        for file in required:


            path = os.path.join(

                project_path,

                file

            )


            result.append(

                {

                "file":

                    file,


                "exists":

                    os.path.exists(path)

                }

            )



        return result