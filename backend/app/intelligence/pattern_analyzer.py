from collections import Counter
from typing import Any



class PatternAnalyzer:

    """
    ASEO Pattern Analyzer v1

    Responsible for discovering
    repeated engineering patterns
    from project experiences.

    Input:

    - Knowledge items
    - Agent memories
    - Project results

    Output:

    - Technology patterns
    - Architecture patterns
    - Common problems
    - Successful solutions
    """



    def __init__(self):

        pass



    # =============================================
    # Extract Technologies
    # =============================================


    def extract_technologies(

        self,

        knowledge_items: list[dict]

    ) -> dict:


        technologies = []



        for item in knowledge_items:


            knowledge = item.get(

                "knowledge",

                {}

            )


            architecture = knowledge.get(

                "architecture",

                {}

            )


            if isinstance(

                architecture,

                dict

            ):


                for value in architecture.values():


                    if isinstance(

                        value,

                        str

                    ):

                        technologies.append(

                            value

                        )



        return self.rank_items(

            technologies

        )



    # =============================================
    # Extract Problems
    # =============================================


    def extract_problems(

        self,

        knowledge_items: list[dict]

    ) -> dict:


        problems = []



        for item in knowledge_items:


            knowledge = item.get(

                "knowledge",

                {}

            )


            error = knowledge.get(

                "error"

            )


            if error:

                problems.append(

                    error

                )



        return self.rank_items(

            problems

        )



    # =============================================
    # Extract Successful Patterns
    # =============================================


    def analyze_success_patterns(

        self,

        knowledge_items: list[dict]

    ) -> dict:


        return {

            "technologies":

                self.extract_technologies(

                    knowledge_items

                ),


            "problems":

                self.extract_problems(

                    knowledge_items

                ),


            "total_examples":

                len(

                    knowledge_items

                )

        }



    # =============================================
    # Ranking
    # =============================================


    def rank_items(

        self,

        items: list[Any]

    ) -> dict:


        if not items:

            return {}



        counter = Counter(

            items

        )


        return dict(

            counter.most_common()

        )