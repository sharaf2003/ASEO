class ProjectStore:
    """
    ASEO Project Storage v19.3
    """



    def __init__(
        self
    ):

        self.projects = {}





    def save(
        self,
        project
    ):


        self.projects[

            project.id

        ] = project



        return project.to_dict()





    def get(
        self,
        project_id
    ):


        project = self.projects.get(

            project_id

        )


        if project:

            return project.to_dict()


        return None






    def all(
        self
    ):


        return [

            project.to_dict()

            for project

            in self.projects.values()

        ]