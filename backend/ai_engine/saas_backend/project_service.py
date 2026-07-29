from ai_engine.database import (
    SessionLocal,
    ProjectModel
)

from uuid import uuid4



class ProjectService:
    """
    ASEO Project Service v19.9
    """



    def create_project(
        self,
        name
    ):

        db = SessionLocal()


        project = ProjectModel(

            id=str(uuid4()),

            name=name,

            status="created",

            quality=0

        )


        db.add(project)

        db.commit()

        db.refresh(project)

        db.close()


        return {

            "id":
                project.id,

            "project":
                project.name,

            "status":
                project.status

        }