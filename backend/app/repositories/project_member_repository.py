"""
ASEO Generated Module

Project Member repository layer.
"""


from sqlalchemy.orm import Session

from app.models.project_member import ProjectMember





class ProjectMemberRepository:
    """
    Handles database operations
    for project members.
    """



    # ==========================
    # Create Member
    # ==========================


    def create(

        self,

        db: Session,

        member: ProjectMember

    ) -> ProjectMember:


        try:

            db.add(member)

            db.commit()

            db.refresh(member)


            return member


        except Exception:

            db.rollback()

            raise





    # ==========================
    # Get Project Members
    # ==========================


    def get_project_members(

        self,

        db: Session,

        project_id: int

    ) -> list[ProjectMember]:


        return (

            db.query(ProjectMember)

            .filter(

                ProjectMember.project_id == project_id,

                ProjectMember.status == "ACTIVE"

            )

            .all()

        )





    # ==========================
    # Get Single Member
    # ==========================


    def get_member(

        self,

        db: Session,

        project_id: int,

        user_id: int

    ) -> ProjectMember | None:


        return (

            db.query(ProjectMember)

            .filter(

                ProjectMember.project_id == project_id,

                ProjectMember.user_id == user_id

            )

            .first()

        )





    # ==========================
    # Soft Remove Member
    # ==========================


    def remove(

        self,

        db: Session,

        project_id: int,

        user_id: int

    ) -> ProjectMember | None:


        member = self.get_member(

            db,

            project_id,

            user_id

        )


        if not member:

            return None



        try:

            member.status = "REMOVED"

            db.commit()

            db.refresh(member)


            return member



        except Exception:

            db.rollback()

            raise