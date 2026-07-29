class ProjectPlanner:
    """
    ASEO Project Planner v2

    Converts knowledge into
    software development plan.

    """



    def create_plan(
        self,
        summary
    ):


        phases = []



        actors = summary.get(
            "actors",
            []
        )


        entities = summary.get(
            "entities",
            []
        )





        # =================================
        # Phase 1: Authentication
        # =================================

        if (
            "admin" in actors
            or
            "user" in actors
        ):


            phases.append(

                {

                    "phase":
                        "Authentication & User Management",


                    "priority":
                        "high",


                    "tasks":
                    [

                        {

                            "name":
                                "Design User Entity",

                            "priority":
                                "high"

                        },


                        {

                            "name":
                                "Create Authentication System",

                            "priority":
                                "high"

                        },


                        {

                            "name":
                                "Implement User APIs",

                            "priority":
                                "medium"

                        }

                    ]

                }

            )







        # =================================
        # Business Entities
        # =================================


        for entity in entities:



            if entity in [

                "users"

            ]:

                continue





            phases.append(

                {

                    "phase":

                        f"{entity.capitalize()} Management",



                    "priority":

                        "high",




                    "tasks":

                    [

                        {

                            "name":
                                f"Design {entity} Entity",


                            "priority":
                                "high"

                        },


                        {

                            "name":
                                f"Create {entity} Database Model",


                            "priority":
                                "high"

                        },


                        {

                            "name":
                                f"Build {entity} APIs",


                            "priority":
                                "medium"

                        },


                        {

                            "name":
                                f"Add {entity} Validation Rules",


                            "priority":
                                "medium"

                        }

                    ]

                }

            )




        return phases