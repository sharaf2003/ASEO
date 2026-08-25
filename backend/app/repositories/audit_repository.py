from sqlalchemy.orm import Session


from app.models.audit_log import AuditLog





class AuditRepository:

    """
    ASEO Audit Log Repository.
    """



    # =====================================
    # Create Audit Log
    # =====================================


    def create(

        self,

        db: Session,

        audit_log: AuditLog

    ):


        db.add(audit_log)

        db.commit()

        db.refresh(audit_log)


        return audit_log





    # =====================================
    # Get Organization Logs
    # =====================================


    def get_by_organization(

        self,

        db: Session,

        organization_id: int

    ):


        return (

            db.query(AuditLog)

            .filter(

                AuditLog.organization_id == organization_id

            )

            .order_by(

                AuditLog.created_at.desc()

            )

            .all()

        )





    # =====================================
    # Get User Logs
    # =====================================


    def get_by_user(

        self,

        db: Session,

        user_id: int

    ):


        return (

            db.query(AuditLog)

            .filter(

                AuditLog.user_id == user_id

            )

            .order_by(

                AuditLog.created_at.desc()

            )

            .all()

        )