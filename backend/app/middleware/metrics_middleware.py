import time

from datetime import datetime

from starlette.middleware.base import BaseHTTPMiddleware


class MetricsMiddleware(BaseHTTPMiddleware):

    """
    ASEO Request Metrics Middleware.

    Tracks:
    - Total requests
    - Failed requests
    - Response time
    """


    total_requests = 0

    failed_requests = 0

    total_response_time = 0.0

    started_at = datetime.utcnow()



    async def dispatch(

        self,

        request,

        call_next

    ):


        start_time = time.time()


        MetricsMiddleware.total_requests += 1



        response = None


        try:


            response = await call_next(

                request

            )


            if response.status_code >= 400:

                MetricsMiddleware.failed_requests += 1



            return response



        finally:


            process_time = time.time() - start_time


            MetricsMiddleware.total_response_time += process_time


            if response:

                response.headers["X-Process-Time"] = str(

                    round(

                        process_time,

                        4

                    )

                )