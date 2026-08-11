"""
ASEO Generated Module

Project Invitation repository layer.
"""


from sqlalchemy.orm import Session


from app.models.project_invitation import ProjectInvitation





class ProjectInvitationRepository:
    """
    Handles database operations
    for project invitations.
    """



    # ==========================
    # Create Invitation
    # ==========================


    def create(

        self,

        db: Session,

        invitation: ProjectInvitation

    ) -> ProjectInvitation:


        try:

            db.add(invitation)

            db.commit()

            db.refresh(invitation)


            return invitation


        except Exception:

            db.rollback()

            raise





    # ==========================
    # Get Invitation By ID
    # ==========================


    def get_by_id(

        self,

        db: Session,

        invitation_id: int

    ) -> ProjectInvitation | None:


        return (

            db.query(ProjectInvitation)

            .filter(

                ProjectInvitation.id == invitation_id

            )

            .first()

        )





    # ==========================
    # Get Project Invitations
    # ==========================


    def get_project_invitations(

        self,

        db: Session,

        project_id: int

    ) -> list[ProjectInvitation]:


        return (

            db.query(ProjectInvitation)

            .filter(

                ProjectInvitation.project_id == project_id

            )

            .all()

        )





    # ==========================
    # Find Pending Invitation
    # ==========================


    def get_pending_by_email(

        self,

        db: Session,

        project_id: int,

        email: str

    ) -> ProjectInvitation | None:


        return (

            db.query(ProjectInvitation)

            .filter(

                ProjectInvitation.project_id == project_id,

                ProjectInvitation.email == email,

                ProjectInvitation.status == "PENDING"

            )

            .first()

        )





    # ==========================
    # Update Invitation Status
    # ==========================


    def update_status(

        self,

        db: Session,

        invitation: ProjectInvitation,

        status: str

    ) -> ProjectInvitation:


        try:

            invitation.status = status

            db.commit()

            db.refresh(invitation)


            return invitation


        except Exception:

            db.rollback()

            raise