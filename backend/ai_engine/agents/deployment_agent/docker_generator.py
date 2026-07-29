class DockerGenerator:
    """
    ASEO Docker Generator v1
    """

    def generate(
        self,
        project_path
    ):

        files = {}



        files["Dockerfile"] = """
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
"""



        files["docker-compose.yml"] = """
version: "3.9"

services:

  backend:

    build: .

    ports:
      - "8000:8000"

    env_file:
      - .env
"""



        files[".env.example"] = """
DATABASE_URL=postgresql://user:password@localhost/db
SECRET_KEY=change_me
"""



        return files