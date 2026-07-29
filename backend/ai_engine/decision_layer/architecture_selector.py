class ArchitectureSelector:
    """
    ASEO Architecture Selector v20.1
    """

    def select(
        self,
        requirement
    ):

        text = requirement.lower()


        if "ecommerce" in text:

            return {
                "architecture":
                    "Layered",

                "framework":
                    "FastAPI",

                "database":
                    "PostgreSQL",

                "reason":
                    "Ecommerce requires scalable backend architecture"
            }


        return {

            "architecture":
                "Modular",

            "framework":
                "FastAPI",

            "database":
                "PostgreSQL",

            "reason":
                "Default scalable architecture"

        }