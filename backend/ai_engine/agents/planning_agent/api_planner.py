class APIPlanner:
    """
    ASEO API Planner v1

    Generates REST API specification.

    """



    def create_apis(
        self,
        summary
    ):


        entities = summary.get(
            "entities",
            []
        )


        endpoints = []



        for entity in entities:


            endpoints.extend(

                [

                    {

                        "method":
                            "GET",


                        "endpoint":
                            f"/{entity}"

                    },


                    {

                        "method":
                            "POST",


                        "endpoint":
                            f"/{entity}"

                    },


                    {

                        "method":
                            "PUT",


                        "endpoint":
                            f"/{entity}/{{id}}"

                    },


                    {

                        "method":
                            "DELETE",


                        "endpoint":
                            f"/{entity}/{{id}}"

                    }

                ]

            )



        return endpoints