from .project_blueprint import (
    ProjectBlueprint
)



class SoftwareCreator:
    """
    ASEO Software Creator v17.1
    """



    def create_blueprint(
        self,
        decision
    ):


        blueprint = ProjectBlueprint(

            name="generated_project",


            architecture=
                decision["architecture"],


            framework=
                decision["framework"],


            database=
                decision["database"],


            modules=[

                "authentication",

                "users",

                "products",

                "orders"

            ]

        )


        return blueprint.to_dict()