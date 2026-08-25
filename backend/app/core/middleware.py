import time
import uuid

from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import settings



# =========================
# Metrics Storage
# =========================

class RequestMetrics:

    total_requests = 0

    failed_requests = 0

    total_response_time = 0.0



# =========================
# Middleware Setup
# =========================

def setup_middleware(

    app: FastAPI

):

    """
    ASEO Middleware Configuration

    Includes:

    - CORS
    - Request ID
    - Security Headers
    - Request Timing
    - Request Metrics
    """



    # =========================
    # CORS
    # =========================


    app.add_middleware(

        CORSMiddleware,

        allow_origins=settings.CORS_ORIGINS,

        allow_credentials=True,

        allow_methods=[

            "*"

        ],

        allow_headers=[

            "*"

        ],

    )





    # =========================
    # Request Middleware
    # =========================


    @app.middleware(

        "http"

    )

    async def aseo_request_middleware(

        request: Request,

        call_next

    ):


        start_time = time.time()



        RequestMetrics.total_requests += 1




        request_id = str(

            uuid.uuid4()

        )



        request.state.request_id = request_id





        response = await call_next(

            request

        )





        if response.status_code >= 400:


            RequestMetrics.failed_requests += 1





        process_time = (

            time.time()

            -

            start_time

        )





        RequestMetrics.total_response_time += process_time





        # =====================
        # Security Headers
        # =====================


        response.headers[

            "X-Request-ID"

        ] = request_id





        response.headers[

            "X-Process-Time"

        ] = str(

            round(

                process_time,

                4

            )

        )





        response.headers[

            "X-Content-Type-Options"

        ] = "nosniff"





        response.headers[

            "X-Frame-Options"

        ] = "DENY"





        response.headers[

            "X-XSS-Protection"

        ] = "1; mode=block"





        return response