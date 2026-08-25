from datetime import datetime

from sqlalchemy.orm import Session

from app.models.api_key import APIKey





class APIKeyRepository:

    """
    Repository for ASEO external API keys.
    """



    # =====================================
    # Create API Key
    # =====================================


    def create(

        self,

        db: Session,

        api_key: APIKey

    ) -> APIKey:


        db.add(api_key)

        db.commit()

        db.refresh(api_key)


        return api_key





    # =====================================
    # Get API Key By Hash
    # =====================================


    def get_by_hash(

        self,

        db: Session,

        key_hash: str

    ) -> APIKey | None:


        return (

            db.query(APIKey)

            .filter(

                APIKey.key_hash == key_hash

            )

            .first()

        )





    # =====================================
    # Get Organization Keys
    # =====================================


    def get_by_organization(

        self,

        db: Session,

        organization_id: int

    ) -> list[APIKey]:


        return (

            db.query(APIKey)

            .filter(

                APIKey.organization_id == organization_id

            )

            .all()

        )





    # =====================================
    # Update Last Used
    # =====================================


    def update_last_used(

        self,

        db: Session,

        api_key: APIKey

    ) -> APIKey:


        api_key.last_used_at = datetime.utcnow()


        db.commit()

        db.refresh(api_key)


        return api_key





    # =====================================
    # Disable API Key
    # =====================================


    def deactivate(

        self,

        db: Session,

        api_key: APIKey

    ) -> APIKey:


        api_key.status = "inactive"


        db.commit()

        db.refresh(api_key)


        return api_key


    def get_by_id(
        self,
        db: Session,
        api_key_id: int
    ):
        return (
            db.query(APIKey)
            .filter(
                APIKey.id == api_key_id
            )
            .first()
        )