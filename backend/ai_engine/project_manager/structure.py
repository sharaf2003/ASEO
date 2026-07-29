class ProjectStructure:
    """
    ASEO Project Structure Definition v15
    """

    def __init__(self):

        self.directories = [

            "backend/app",

            "backend/app/models",

            "backend/app/routes",

            "backend/app/services",

            "backend/app/schemas",

            "tests"

        ]


        self.files = [

            "backend/app/main.py",

            "backend/app/database.py",

            "requirements.txt",

            "Dockerfile",

            "README.md"

        ]