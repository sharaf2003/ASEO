from sqlalchemy.orm import Session

from app.models.api_rate_limit import APIRateLimit





class APIRateLimitRepository:

    """
    ASEO API Rate Limit Repository.
    """



    def create(

        self,

        db: Session,

        rate_limit: APIRateLimit

    ):

        db.add(

            rate_limit

        )

        db.commit()

        db.refresh(

            rate_limit

        )

        return rate_limit





    def get_by_api_key(

        self,

        db: Session,

        api_key_id: int

    ):


        return (

            db.query(APIRateLimit)

            .filter(

                APIRateLimit.api_key_id == api_key_id

            )

            .first()

        )





    def update(

        self,

        db: Session,

        rate_limit: APIRateLimit,

        data: dict

    ):


        for key, value in data.items():

            setattr(

                rate_limit,

                key,

                value

            )


        db.commit()

        db.refresh(

            rate_limit

        )

        return rate_limit





    def delete(

        self,

        db: Session,

        rate_limit: APIRateLimit

    ):


        db.delete(

            rate_limit

        )

        db.commit()