from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.database.session import get_database

from app.schemas.auth import (
    TokenResponse,
)

from app.schemas.register import (
    RegisterRequest,
    RegisterResponse,
)

from app.services.auth_service import (
    AuthService,
)

from app.services.register_service import (
    RegisterService,
)


router = APIRouter()

auth_service = AuthService()

register_service = RegisterService()


# =====================================================
# User Register
# =====================================================

@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register New Customer",
    description="""
Create new ASEO customer:

- Organization
- Default Workspace
- Owner User
""",
)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_database),
):

    try:

        user = register_service.register(
            db,
            data,
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


    return {
        "message": "Registration completed successfully",
        "user_id": user.id,
        "organization_id": user.organization_id,
        "workspace_id": user.workspace_id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
    }


# =====================================================
# User Login
# =====================================================

@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="User Login",
    description="Authenticate user and generate JWT access token.",
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_database),
):

    try:

        return auth_service.login(
            db,
            form_data.username,
            form_data.password,
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
            headers={
                "WWW-Authenticate": "Bearer"
            },
        ) from exc