from sqlalchemy.orm import Session


from app.models.user import User

from app.security.password import hash_password

from app.repositories.user_repository import (
    UserRepository
)





class UserService:
    """
    Service layer for ASEO users.
    """



    def __init__(self):

        self.repository = UserRepository()





    def create_user(

        self,

        db: Session,

        data,

        organization_id: int,

        workspace_id: int

    ):


        existing_user = self.repository.get_by_email(

            db,

            data.email

        )



        if existing_user:

            raise Exception(

                "User already exists"

            )





        user = User(

            name=data.name,

            organization_id=organization_id,

            workspace_id=workspace_id,

            email=data.email,

            password_hash=hash_password(data.password),

            role=data.role

        )



        return self.repository.create(

            db,

            user

        )







    def get_users(

        self,

        db: Session,

        organization_id: int

    ):


        return self.repository.get_all(

            db,

            organization_id

        )







    def get_workspace_users(

        self,

        db: Session,

        workspace_id: int,

        organization_id: int

    ):


        return self.repository.get_by_workspace(

            db,

            workspace_id,

            organization_id

        )