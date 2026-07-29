from sqlalchemy.orm import Session

from app.models.organization import Organization





class OrganizationRepository:
    """
    Repository for tenant organizations.
    """



    def create(

        self,

        db: Session,

        organization: Organization

    ):


        db.add(organization)

        db.commit()

        db.refresh(organization)


        return organization





    def get_by_id(

        self,

        db: Session,

        organization_id: int

    ):


        return db.query(

            Organization

        ).filter(

            Organization.id == organization_id

        ).first()