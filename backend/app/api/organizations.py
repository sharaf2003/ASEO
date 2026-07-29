from fastapi import (
    APIRouter,
    Depends,
    status
)


from sqlalchemy.orm import Session


from app.security.dependencies import (
    get_current_user
)


from app.security.roles import (
    require_role
)


from app.database.session import get_database


from app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse
)


from app.services.organization_service import (
    OrganizationService
)





router = APIRouter()



service = OrganizationService()





# ==========================
# Create Organization
# OWNER ONLY
# ==========================


@router.post(
    "",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Organization"
)
def create_organization(

    organization: OrganizationCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    return service.create_organization(

        db,

        organization

    )





# ==========================
# Get Current Organization
# AUTHENTICATED USERS
# ==========================


@router.get(
    "",
    response_model=OrganizationResponse,
    summary="Get Current Organization"
)
def get_current_organization(

    db: Session = Depends(get_database),

    current_user: dict = Depends(get_current_user)

):


    return service.get_organization(

        db,

        current_user["organization_id"]

    )