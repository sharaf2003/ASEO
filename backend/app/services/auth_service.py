from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    UserRepository
)

from app.security.password import (
    verify_password
)

from app.security.jwt import (
    create_access_token
)


class AuthService:
    """
    Authentication service for ASEO users.
    """


    def __init__(self):

        self.repository = UserRepository()



    def login(
        self,
        db: Session,
        email: str,
        password: str
    ):

        # Normalize email

        email = email.lower().strip()



        user = self.repository.get_by_email(
            db,
            email
        )



        if not user:

            raise ValueError(
                "Invalid credentials"
            )



        if not verify_password(
            password,
            user.password_hash
        ):

            raise ValueError(
                "Invalid credentials"
            )



        if not user.role:

            raise ValueError(
                "User role is not configured"
            )



        token = create_access_token({

            "sub": str(user.id),

            "email": user.email,

            "role": user.role,

            "organization_id": user.organization_id,

            "workspace_id": user.workspace_id

        })



        return {

            "access_token": token,

            "token_type": "bearer",

            "user": {

                "id": user.id,

                "name": user.name,

                "email": user.email,

                "role": user.role,

                "organization_id": user.organization_id,

                "workspace_id": user.workspace_id

            }

        }