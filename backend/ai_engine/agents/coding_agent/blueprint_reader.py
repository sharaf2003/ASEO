class BlueprintReader:
    """
    ASEO Blueprint Reader v1

    Reads Planning Agent output.

    """



    def extract_structure(
        self,
        blueprint
    ):


        return blueprint.get(
            "project_structure",
            []
        )





    def extract_entities(
        self,
        blueprint
    ):


        database = blueprint.get(
            "database_design",
            {}
        )


        return database.get(
            "tables",
            []
        )





    def extract_apis(
        self,
        blueprint
    ):


        return blueprint.get(
            "api_design",
            []
        )