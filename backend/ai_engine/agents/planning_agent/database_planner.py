class DatabasePlanner:
    """
    ASEO Database Planner v1

    Generates database design.

    """



    def create_schema(
        self,
        summary
    ):


        entities = summary.get(
            "entities",
            []
        )


        tables = []



        for entity in entities:


            tables.append(

                {

                    "table":

                        entity,


                    "fields":

                    [

                        "id",

                        "created_at",

                        "updated_at"

                    ]

                }

            )



        return {


            "database":

                "PostgreSQL",


            "tables":

                tables

        }