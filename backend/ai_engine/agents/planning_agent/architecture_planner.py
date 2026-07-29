class ArchitecturePlanner:
    """
    ASEO Architecture Planner v1

    Generates software architecture
    from project knowledge.

    """



    def create_architecture(
        self,
        summary
    ):


        actors = summary.get(
            "actors",
            []
        )


        entities = summary.get(
            "entities",
            []
        )



        return {


            "backend":

                "FastAPI",



            "database":

                "PostgreSQL",



            "architecture_pattern":

                "MVC",



            "authentication":

                "JWT",



            "entities":

                entities,



            "actors":

                actors


        }