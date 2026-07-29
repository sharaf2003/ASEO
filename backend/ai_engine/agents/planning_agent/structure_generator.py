class StructureGenerator:
    """
    ASEO Project Structure Generator v1

    Generates backend structure.
    """



    def generate(
        self,
        architecture
    ):


        backend = architecture.get(
            "backend",
            ""
        )


        if backend == "FastAPI":


            return [

                "app/",

                "app/models/",

                "app/schemas/",

                "app/routes/",

                "app/services/",

                "app/repositories/",

                "app/database/",

                "tests/",

                "requirements.txt"

            ]



        return []