from app.repositories.knowledge_repository import (
    KnowledgeRepository
)


class KnowledgeManager:


    def __init__(

        self,

        db

    ):


        self.repository = KnowledgeRepository(

            db

        )



    def store_patterns(

        self,

        patterns: list

    ) -> list:


        stored = []


        for pattern in patterns:


            architecture = pattern.get(

                "architecture",

                {}

            )


            signature = pattern.get(

                "signature",

                "unknown"

            )


            total_usage = pattern.get(

                "total_usage",

                0

            )


            average_success = pattern.get(

                "average_success",

                0

            )


            metadata = {


                "signature": signature,


                "total_usage": total_usage,


                "memory_count": pattern.get(

                    "memory_count",

                    0

                )

            }



            saved_pattern = (

                self.repository
                .add_pattern(

                    category="architecture_pattern",

                    name=signature,

                    success=(

                        average_success >= 0.7

                    ),

                    metadata=metadata,

                    context=architecture

                )

            )



            stored.append(

                saved_pattern

            )



        return stored