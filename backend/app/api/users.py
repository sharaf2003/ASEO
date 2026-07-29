from fastapi import (
    APIRouter,
    Depends,
    status
)


from sqlalchemy.orm import Session


from app.security.roles import (
    require_role
)


from app.database.session import get_database


from app.schemas.user import (
    UserCreate,
    UserResponse
)


from app.services.user_service import (
    UserService
)





router = APIRouter()



service = UserService()





# ==========================
# Create User
# OWNER ONLY
# ==========================


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create User"
)
def create_user(

    user: UserCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    return service.create_user(

        db,

        user,

        current_user["organization_id"],

        current_user["workspace_id"]


    )





# ==========================
# Get Organization Users
# OWNER ONLY
# ==========================


@router.get(
    "",
    response_model=list[UserResponse],
    summary="Get Organization Users"
)
def list_users(

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    return service.get_users(

        db,

        current_user["organization_id"]

    )





# ==========================
# Get Workspace Users
# OWNER ONLY
# ==========================


@router.get(
    "/workspace/{workspace_id}",
    response_model=list[UserResponse],
    summary="Get Workspace Users"
)
def list_workspace_users(

    workspace_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    return service.get_workspace_users(

        db,

        workspace_id,

        current_user["organization_id"]

    )