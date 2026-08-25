from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.api_usage import APIUsage


from app.models.api_key import APIKey


class APIUsageRepository:

    """
    Repository for ASEO API usage tracking.
    """



    # =====================================
    # Create Usage Record
    # =====================================


    def create(

        self,

        db: Session,

        usage: APIUsage

    ) -> APIUsage:


        db.add(usage)

        db.commit()

        db.refresh(usage)


        return usage





    # =====================================
    # Get Usage By API Key
    # =====================================


    def get_by_api_key(

        self,

        db: Session,

        api_key_id: int

    ) -> list[APIUsage]:


        return (

            db.query(APIUsage)

            .filter(

                APIUsage.api_key_id == api_key_id

            )

            .order_by(

                APIUsage.created_at.desc()

            )

            .all()

        )





    # =====================================
    # Count Requests
    # =====================================


    def get_request_count(

        self,

        db: Session,

        api_key_id: int

    ) -> int:


        records = (

            db.query(APIUsage)

            .filter(

                APIUsage.api_key_id == api_key_id

            )

            .all()

        )


        return sum(

            item.requests_count

            for item in records

        )





    # =====================================
    # Usage Between Dates
    # =====================================


    def get_between_dates(

        self,

        db: Session,

        api_key_id: int,

        start_date: datetime,

        end_date: datetime

    ) -> list[APIUsage]:


        return (

            db.query(APIUsage)

            .filter(

                APIUsage.api_key_id == api_key_id,

                APIUsage.created_at >= start_date,

                APIUsage.created_at <= end_date

            )

            .order_by(

                APIUsage.created_at.asc()

            )

            .all()

        )

    
    # =====================================
    # Get Organization Usage By Month
    # =====================================


    def get_by_organization_month(

        self,

        db: Session,

        organization_id: int,

        month: str

    ) -> list[APIUsage]:


        start_date = datetime.strptime(

            month + "-01",

            "%Y-%m-%d"

        )



        if start_date.month == 12:

            end_date = start_date.replace(

                year=start_date.year + 1,

                month=1

            )

        else:

            end_date = start_date.replace(

                month=start_date.month + 1

            )





        return (

            db.query(APIUsage)

            .join(

                APIKey,

                APIUsage.api_key_id == APIKey.id

            )

            .filter(

                APIKey.organization_id == organization_id,

                APIUsage.created_at >= start_date,

                APIUsage.created_at < end_date

            )

            .order_by(

                APIUsage.created_at.asc()

            )

            .all()

        )

    # =====================================
    # Requests Last Minute
    # =====================================

    def get_requests_last_minute(

        self,

        db: Session,

        api_key_id: int

    ) -> int:


        start = datetime.utcnow() - timedelta(minutes=1)


        records = (

            db.query(APIUsage)

            .filter(

                APIUsage.api_key_id == api_key_id,

                APIUsage.created_at >= start

            )

            .all()

        )


        return sum(

            item.requests_count

            for item in records

        )





    # =====================================
    # Requests Today
    # =====================================

    def get_requests_today(

        self,

        db: Session,

        api_key_id: int

    ) -> int:


        start = datetime.utcnow().replace(

            hour=0,

            minute=0,

            second=0,

            microsecond=0

        )


        records = (

            db.query(APIUsage)

            .filter(

                APIUsage.api_key_id == api_key_id,

                APIUsage.created_at >= start

            )

            .all()

        )


        return sum(

            item.requests_count

            for item in records

        )





    # =====================================
    # Requests This Month
    # =====================================

    def get_requests_this_month(

        self,

        db: Session,

        api_key_id: int

    ) -> int:


        now = datetime.utcnow()


        start = now.replace(

            day=1,

            hour=0,

            minute=0,

            second=0,

            microsecond=0

        )


        records = (

            db.query(APIUsage)

            .filter(

                APIUsage.api_key_id == api_key_id,

                APIUsage.created_at >= start

            )

            .all()

        )


        return sum(

            item.requests_count

            for item in records

        )