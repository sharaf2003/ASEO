from sqlalchemy.orm import Session

from app.models.project import Project

from app.models.project_member import ProjectMember



class ProjectRepository:
    """
    Handles database operations
    related to projects.
    """



    def create(
        self,
        db: Session,
        project: Project
    ):


        db.add(project)

        db.commit()

        db.refresh(project)


        return project





    def get_all(
        self,
        db: Session,
        organization_id: int | None = None
    ):


        query = db.query(Project)



        if organization_id is not None:

            query = query.filter(

                Project.organization_id == organization_id

            )



        return query.all()





    def get_by_id(
        self,
        db: Session,
        project_id: int,
        organization_id: int
    ):


        return db.query(Project).filter(

            Project.id == project_id,

            Project.organization_id == organization_id

        ).first()

    def get_my_projects(
        self,
        db: Session,
        user_id: int
    ):

        return (
            db.query(Project)
            .outerjoin(
                ProjectMember,
                Project.id == ProjectMember.project_id
            )
            .filter(
                (Project.owner_id == user_id)
                |
                (ProjectMember.user_id == user_id)
            )
            .distinct()
            .all()
        )
    def update(
        self,
        db: Session,
        project: Project
    ):

        db.commit()

        db.refresh(project)

        return project