class ProjectStore:
    """
    ASEO Project Store v1
    """



    def __init__(self):

        self.projects = {}




    def save(
        self,
        project_id,
        data
    ):


        self.projects[project_id] = data




    def get(
        self,
        project_id
    ):


        return self.projects.get(
            project_id
        )