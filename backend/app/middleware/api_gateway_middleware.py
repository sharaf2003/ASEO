from fastapi import Request

from fastapi.responses import JSONResponse

from starlette.middleware.base import (
    BaseHTTPMiddleware
)


from sqlalchemy.orm import Session


from app.database.session import (
    SessionLocal
)


from app.services.api_gateway_service import (
    APIGatewayService
)





class APIGatewayMiddleware(BaseHTTPMiddleware):

    """
    ASEO SaaS API Gateway Middleware.

    Responsibilities:

    - Authenticate API Keys
    - Validate Subscription
    - Apply Rate Limits
    - Track Usage
    """



    PUBLIC_PATHS = [

        "/health",

        "/docs",

        "/openapi.json",

        "/redoc"

    ]





    def __init__(

        self,

        app

    ):

        super().__init__(app)

        self.gateway_service = APIGatewayService()





    async def dispatch(

        self,

        request: Request,

        call_next

    ):


        # Ignore public routes

        if request.url.path in self.PUBLIC_PATHS:

            return await call_next(

                request

            )




        api_key = request.headers.get(

            "X-API-Key"

        )




        # Internal requests without API Key

        if not api_key:

            return await call_next(

                request

            )





        db: Session = SessionLocal()



        try:


            # Authenticate API Key

            key = self.gateway_service.authenticate_api_key(

                db,

                api_key

            )





            if not key:


                return JSONResponse(

                    status_code=401,

                    content={

                        "detail": "Invalid API Key"

                    }

                )





            # Check Subscription

            self.gateway_service.check_subscription_access(

                db,

                key

            )





            # Check Rate Limit

            rate = self.gateway_service.check_rate_limit(

                db,

                key

            )





            if not rate["allowed"]:


                return JSONResponse(

                    status_code=429,

                    content={

                        "detail": "Rate limit exceeded",

                        "reason": rate.get(

                            "reason",

                            "unknown"

                        )

                    }

                )





            # Record Usage

            self.gateway_service.record_usage(

                db,

                key,

                request.url.path

            )





            response = await call_next(

                request

            )


            return response





        except Exception as e:


            return JSONResponse(

                status_code=500,

                content={

                    "detail": "API Gateway Error"

                }

            )





        finally:


            db.close()