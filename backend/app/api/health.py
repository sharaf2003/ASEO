"""
ASEO Health & Metrics API.
"""


from fastapi import APIRouter


from app.core.middleware import (
    RequestMetrics
)


router = APIRouter()



# =====================================
# Health Check
# =====================================


@router.get(

    "/health",

    tags=["Health"]

)
def health_check():

    return {

        "status": "healthy",

        "service": "aseo_backend"

    }




# =====================================
# Metrics
# =====================================


@router.get(

    "/metrics",

    tags=["Monitoring"]

)
def metrics():


    total_requests = RequestMetrics.total_requests


    failed_requests = RequestMetrics.failed_requests


    total_time = RequestMetrics.total_response_time



    average_response_time = (

        total_time / total_requests

        if total_requests > 0

        else 0

    )



    return {

        "status": "running",

        "total_requests": total_requests,

        "failed_requests": failed_requests,

        "average_response_time": round(

            average_response_time,

            4

        )

    }