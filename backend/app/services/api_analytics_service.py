from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.repositories.api_usage_repository import (
    APIUsageRepository
)





class APIAnalyticsService:

    """
    ASEO API Analytics Service.

    Provides API usage insights.
    """



    def __init__(self):

        self.api_usage_repository = APIUsageRepository()





    def get_api_key_analytics(

        self,

        db: Session,

        api_key_id: int

    ):


        now = datetime.utcnow()



        start_today = datetime(

            now.year,

            now.month,

            now.day

        )



        start_month = datetime(

            now.year,

            now.month,

            1

        )



        all_usage = (

            self.api_usage_repository.get_by_api_key(

                db,

                api_key_id

            )

        )



        today_usage = (

            self.api_usage_repository.get_between_dates(

                db,

                api_key_id,

                start_today,

                now

            )

        )



        month_usage = (

            self.api_usage_repository.get_between_dates(

                db,

                api_key_id,

                start_month,

                now

            )

        )



        endpoint_counter = {}



        for item in all_usage:

            endpoint_counter[item.endpoint] = (

                endpoint_counter.get(

                    item.endpoint,

                    0

                )

                + item.requests_count

            )



        top_endpoints = sorted(

            endpoint_counter.items(),

            key=lambda x: x[1],

            reverse=True

        )[:5]



        return {

            "api_key_id": api_key_id,


            "total_requests":

                sum(

                    item.requests_count

                    for item in all_usage

                ),


            "today_requests":

                sum(

                    item.requests_count

                    for item in today_usage

                ),


            "month_requests":

                sum(

                    item.requests_count

                    for item in month_usage

                ),


            "last_request":

                (

                    all_usage[0].created_at

                    if all_usage

                    else None

                ),


            "top_endpoints":

                [

                    {

                        "endpoint": endpoint,

                        "count": count

                    }

                    for endpoint, count in top_endpoints

                ]

        }