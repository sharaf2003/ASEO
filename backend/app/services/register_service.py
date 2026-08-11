from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.organization import Organization
from app.models.workspace import Workspace
from app.models.user import User

from app.security.password import hash_password

from app.repositories.user_repository import UserRepository


class RegisterService:

    def __init__(self):

        self.user_repository = UserRepository()


    def register(
        self,
        db: Session,
        data
    ):

        # =================================================
        # Normalize Input
        # =================================================

        email = data.email.lower().strip()


        # =================================================
        # Check Existing User
        # =================================================

        existing_user = self.user_repository.get_by_email(
            db,
            email
        )

        if existing_user:

            raise ValueError(
                "A user with this email already exists"
            )


        try:

            # =============================================
            # Create Organization
            # =============================================

            organization = Organization(
                name=data.organization_name,
                plan="free"
            )

            db.add(organization)

            # Send INSERT to database without COMMIT.
            # This gives us organization.id while keeping
            # the whole registration in one transaction.

            db.flush()


            # =============================================
            # Create Workspace
            # =============================================

            workspace = Workspace(
                organization_id=organization.id,
                name="Production"
            )

            db.add(workspace)

            # Get workspace.id without COMMIT.

            db.flush()


            # =============================================
            # Create Owner User
            # =============================================

            user = User(
                name=data.name,
                organization_id=organization.id,
                workspace_id=workspace.id,
                email=email,
                password_hash=hash_password(
                    data.password
                ),
                role="OWNER"
            )

            db.add(user)


            # =============================================
            # Commit Complete Registration
            # =============================================

            db.commit()

            db.refresh(user)

            return user


        except IntegrityError as exc:

            db.rollback()

            raise ValueError(
                "Registration data conflicts with existing data"
            ) from exc


        except Exception:

            db.rollback()

            raise