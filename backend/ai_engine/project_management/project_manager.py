from .project import Project

from .project_store import ProjectStore





class ProjectManager:
    """
    ASEO Multi Project Manager v19.3

    Manages company projects.
    """



    def __init__(
        self
    ):


        self.store = ProjectStore()





    def create_project(
        self,
        name,
        client
    ):


        project = Project(

            name,

            client

        )



        return self.store.save(

            project

        )







    def assign_team(
        self,
        project_id,
        team
    ):


        project = self.store.projects.get(

            project_id

        )


        if not project:

            return None



        project.assign_team(

            team

        )


        return project.to_dict()






    def update_project(
        self,
        project_id,
        status,
        quality
    ):


        project = self.store.projects.get(

            project_id

        )


        if not project:

            return None



        project.update_status(

            status

        )


        project.set_quality(

            quality

        )


        return project.to_dict()