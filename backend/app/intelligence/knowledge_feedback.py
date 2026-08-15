from app.repositories.knowledge_repository import KnowledgeRepository





class KnowledgeFeedback:

    """
    ASEO Knowledge Feedback Engine

    Responsible for:

    - Evaluating execution results
    - Updating knowledge scores
    - Improving future decisions
    """



    def __init__(

        self,

        db=None

    ):


        self.repository = None



        if db:

            self.repository = KnowledgeRepository(

                db

            )





    # =============================================
    # Update Knowledge Feedback
    # =============================================


    def update(

        self,

        result: dict,

        success: bool

    ):


        if not self.repository:

            return



        patterns = self.extract_patterns(

            result

        )



        for pattern in patterns:


            existing = self.repository.get_pattern_by_name(

                category=pattern["category"],

                name=pattern["name"]

            )



            if existing:


                self.repository.update_pattern_score(

                    pattern_id=existing.id,

                    success=success

                )





    # =============================================
    # Extract Used Patterns
    # =============================================


    def extract_patterns(

        self,

        result: dict

    ) -> list:


        patterns = []



        architecture = result.get(

            "architecture",

            {}

        )



        if isinstance(architecture, dict):


            for layer, values in architecture.items():


                if isinstance(values, dict):


                    for key, value in values.items():


                        if isinstance(value, str):


                            patterns.append(

                                {

                                    "category": key,

                                    "name": value

                                }

                            )



                elif isinstance(values, str):


                    patterns.append(

                        {

                            "category": layer,

                            "name": values

                        }

                    )





        technologies = result.get(

            "technologies",

            []

        )



        for technology in technologies:


            patterns.append(

                {

                    "category": "technology",

                    "name": str(technology)

                }

            )



        return patterns