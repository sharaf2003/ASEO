from sqlalchemy.orm import Session

from app.models.user import User





class UserRepository:
    """
    Repository for ASEO platform users.
    """



    def create(

        self,

        db: Session,

        user: User

    ):


        db.add(user)

        db.commit()

        db.refresh(user)


        return user





    def get_all(

        self,

        db: Session,

        organization_id: int

    ):


        return db.query(

            User

        ).filter(

            User.organization_id == organization_id

        ).all()





    def get_by_workspace(

        self,

        db: Session,

        workspace_id: int,

        organization_id: int

    ):


        return db.query(

            User

        ).filter(

            User.workspace_id == workspace_id,

            User.organization_id == organization_id

        ).all()





    def get_by_email(

        self,

        db: Session,

        email: str

    ):


        return db.query(

            User

        ).filter(

            User.email == email

        ).first()