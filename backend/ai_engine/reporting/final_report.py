class FinalReportGenerator:
    """
    ASEO Final Report Generator v14.1

    Creates unified production reports.
    """



    def generate(
        self,
        project,
        architecture,
        execution,
        learning,
        knowledge
    ):


        evaluation = (

            learning
            .get(
                "evaluation",
                {}
            )

        )


        improvement = (

            learning
            .get(
                "improvement",
                {}

            )

        )



        experience = (

            learning
            .get(
                "experience",
                {}

            )

        )



        return {


            "version":

                "14.1",



            "project":

                project,



            "status":

                "completed",



            "architecture":

                {


                    "framework":

                        architecture
                        .get(
                            "recommendation",
                            {}
                        )
                        .get(
                            "framework"
                        ),



                    "database":

                        architecture
                        .get(
                            "recommendation",
                            {}
                        )
                        .get(
                            "database"
                        ),



                    "confidence":

                        architecture
                        .get(
                            "confidence"
                        )

                },



            "agents":

                evaluation,



            "learning":

                {


                    "saved":

                        bool(
                            experience
                        ),


                    "score":

                        experience
                        .get(
                            "score",
                            0
                        )

                },



            "improvement":

                {


                    "old_score":

                        improvement
                        .get(
                            "old_score",
                            0
                        ),


                    "new_score":

                        improvement
                        .get(
                            "new_score",
                            0
                        ),


                    "improved":

                        improvement
                        .get(
                            "improved",
                            False
                        )

                },



            "knowledge":

                {


                    "updated":

                        bool(
                            knowledge
                        ),


                    "nodes":

                        len(
                            knowledge
                            .get(
                                "nodes",
                                []
                            )
                        )

                }

        }