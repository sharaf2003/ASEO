from sqlalchemy.orm import Session


from app.models.organization import Organization


from app.repositories.organization_repository import (
    OrganizationRepository
)





class OrganizationService:
    """
    Service layer for ASEO tenants.
    """



    def __init__(self):

        self.repository = OrganizationRepository()





    def create_organization(

        self,

        db: Session,

        data

    ):


        organization = Organization(

            name=data.name,

            plan=data.plan

        )



        return self.repository.create(

            db,

            organization

        )





    def get_organization(

        self,

        db: Session,

        organization_id: int

    ):


        return self.repository.get_by_id(

            db,

            organization_id

        )