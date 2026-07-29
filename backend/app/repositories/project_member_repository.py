"""
ASEO Generated Module

Project Member repository layer.
"""


from enum import member

from sqlalchemy.orm import Session


from app.models.project_member import ProjectMember





class ProjectMemberRepository:
    """
    Handles database operations
    for project members.
    """



    def create(

        self,

        db: Session,

        member: ProjectMember

    ):


        db.add(member)

        db.commit()

        db.refresh(member)

        return member





    def get_project_members(

        self,

        db: Session,

        project_id: int

    ):


        return (

            db.query(ProjectMember)

            .filter(
                ProjectMember.project_id == project_id
            )

            .all()

        )





    def get_member(

        self,

        db: Session,

        project_id: int,

        user_id: int

    ):


        return (

            db.query(ProjectMember)

            .filter(

                ProjectMember.project_id == project_id,

                ProjectMember.user_id == user_id

            )

            .first()

        )
    
    def delete(
    self,
    db: Session,
    project_id: int,
    user_id: int
    ):

        member = (
            db.query(ProjectMember)
            .filter(
                ProjectMember.project_id == project_id,
                ProjectMember.user_id == user_id
            )
        .first()
    )

        if not member:
            return None

        db.delete(member)
        db.commit()

        return member