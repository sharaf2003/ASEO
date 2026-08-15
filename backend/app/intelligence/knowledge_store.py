from collections import defaultdict
from datetime import datetime



class KnowledgeStore:

    """
    ASEO Knowledge Store v1

    Stores consolidated knowledge
    extracted from thousands of
    project experiences.

    """



    def __init__(self):

        self.knowledge = {

            "technologies": defaultdict(int),

            "architectures": defaultdict(int),

            "solutions": defaultdict(int),

            "problems": defaultdict(int)

        }



    # =============================================
    # Add Knowledge
    # =============================================


    def add(

        self,

        category: str,

        value: str

    ):


        if category not in self.knowledge:

            self.knowledge[category] = defaultdict(int)



        self.knowledge[category][value] += 1





    # =============================================
    # Add Project Knowledge
    # =============================================


    def learn_from_project(

        self,

        project_knowledge: dict

    ):


        architecture = project_knowledge.get(

            "architecture",

            {}

        )


        if isinstance(architecture, dict):


            for key, value in architecture.items():


                if isinstance(value, str):

                    self.add(

                        "technologies",

                        value

                    )



        problems = project_knowledge.get(

            "problems",

            []

        )


        for problem in problems:


            self.add(

                "problems",

                str(problem)

            )



        solutions = project_knowledge.get(

            "solutions",

            []

        )


        for solution in solutions:


            self.add(

                "solutions",

                str(solution)

            )



    # =============================================
    # Get Knowledge
    # =============================================


    def get_top_patterns(

        self,

        limit: int = 10

    ):


        result = {}



        for category, values in self.knowledge.items():


            result[category] = sorted(

                values.items(),

                key=lambda x: x[1],

                reverse=True

            )[:limit]



        return result



    # =============================================
    # Export
    # =============================================


    def export(self):


        return {

            "created_at":

                datetime.utcnow().isoformat(),


            "knowledge":

                self.get_top_patterns()

        }