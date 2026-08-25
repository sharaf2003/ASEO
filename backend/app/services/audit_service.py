from sqlalchemy.orm import Session


from app.models.audit_log import AuditLog


from app.repositories.audit_repository import (
    AuditRepository
)





class AuditService:

    """
    ASEO Audit Service.

    Handles system activity tracking.
    """





    def __init__(self):

        self.repository = AuditRepository()





    # =====================================
    # Create Audit Event
    # =====================================


    def log_event(

        self,

        db: Session,

        action: str,

        description: str | None = None,

        organization_id: int | None = None,

        user_id: int | None = None

    ):


        audit = AuditLog(

            organization_id=organization_id,

            user_id=user_id,

            action=action,

            description=description

        )



        return self.repository.create(

            db,

            audit

        )





    # =====================================
    # Organization History
    # =====================================


    def get_organization_logs(

        self,

        db: Session,

        organization_id: int

    ):


        return self.repository.get_by_organization(

            db,

            organization_id

        )





    # =====================================
    # User History
    # =====================================


    def get_user_logs(

        self,

        db: Session,

        user_id: int

    ):


        return self.repository.get_by_user(

            db,

            user_id

        )