from fastapi import FastAPI

from .auth_api import router as auth_router

from .project_api import router as project_router

from .api_key_manager import APIKeyManager

from .auth_middleware import AuthMiddleware

from .rate_limiter import RateLimiter

from .usage_tracker import UsageTracker



class ASEOGateway:
    """
    ASEO API Gateway v22.6
    """

    def __init__(self):

        self.app = FastAPI(

            title="ASEO SaaS API",

            version="22.6"

        )


        self.keys = APIKeyManager()

        self.auth = AuthMiddleware()

        self.rate = RateLimiter()

        self.usage = UsageTracker()


        self.register_routes()



    def register_routes(self):

        self.app.include_router(

            auth_router,

            prefix="/auth"

        )


        self.app.include_router(

            project_router,

            prefix="/projects"

        )



    def gateway_request(
        self,
        customer,
        requests
    ):

        key = self.keys.create(

            customer

        )


        auth = self.auth.authenticate(

            key["api_key"]

        )


        rate = self.rate.check(

            requests

        )


        usage = self.usage.track(

            customer,

            requests

        )


        return {

            "key":
                key,

            "authentication":
                auth,

            "rate_limit":
                rate,

            "usage":
                usage,

            "status":
                "accepted"

        }



    def get_app(self):

        return self.app