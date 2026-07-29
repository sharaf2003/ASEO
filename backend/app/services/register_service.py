from sqlalchemy.orm import Session


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


        # Create Organization

        organization = Organization(

            name=data.organization_name,

            plan="free"

        )


        db.add(organization)

        db.commit()

        db.refresh(organization)




        # Create Workspace

        workspace = Workspace(

            organization_id=organization.id,

            name="Production"

        )


        db.add(workspace)

        db.commit()

        db.refresh(workspace)




        # Create Owner User

        user = User(

            name=data.name,

            organization_id=organization.id,

            workspace_id=workspace.id,

            email=data.email,

            password_hash=hash_password(data.password),

            role="OWNER"

        )


        db.add(user)

        db.commit()

        db.refresh(user)



        return user