class DockerManager:
    """
    ASEO Docker Manager v15
    """



    def create_dockerfile(
        self,
        project_name
    ):


        docker_content = """

FROM python:3.12


WORKDIR /app


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


CMD ["uvicorn",
"backend.app.main:app",
"--host",
"0.0.0.0",
"--port",
"8000"]

"""


        return {

            "project":
                project_name,


            "dockerfile_created":
                True,


            "content":
                docker_content

        }