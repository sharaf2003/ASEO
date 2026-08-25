import hashlib
import secrets


from sqlalchemy.orm import Session


from app.models.api_key import APIKey

from app.models.api_usage import APIUsage

from app.models.api_rate_limit import APIRateLimit



from app.repositories.api_key_repository import (
    APIKeyRepository
)


from app.repositories.api_usage_repository import (
    APIUsageRepository
)


from app.repositories.api_rate_limit_repository import (
    APIRateLimitRepository
)



from app.services.subscription_service import (
    SubscriptionService
)

from app.security.subscription_guard import (
    SubscriptionGuard
)

from app.services.audit_service import (
    AuditService
)


class APIGatewayService:

    """
    ASEO SaaS API Gateway Service.

    Responsibilities:

    - Create API keys
    - Authenticate API requests
    - Track API usage
    - Apply dynamic rate limits
    """



    def __init__(self):

        self.api_key_repository = APIKeyRepository()

        self.api_usage_repository = APIUsageRepository()

        self.api_rate_limit_repository = APIRateLimitRepository()

        self.subscription_service = SubscriptionService()

        self.subscription_guard = SubscriptionGuard()

        self.audit_service = AuditService()


    # =====================================================
    # Create API Key
    # =====================================================


    def create_api_key(

        self,

        db: Session,

        organization_id: int,

        name: str

    ):


        raw_key = (

            "aseo_"

            + secrets.token_urlsafe(32)

        )



        key_hash = hashlib.sha256(

            raw_key.encode()

        ).hexdigest()





        api_key = APIKey(

            organization_id=organization_id,

            name=name,

            key_hash=key_hash,

            status="active"

        )





        created = self.api_key_repository.create(

            db,

            api_key

        )





        # =====================================
        # Get Subscription Plan Limits
        # =====================================


        subscription = self.subscription_service.get_subscription(

            db,

            organization_id

        )



        if not subscription:


            subscription = self.subscription_service.create_default_subscription(

                db,

                organization_id

            )





        limits = self.subscription_service.get_plan_limits(

            subscription.plan

        )





        rate_limit = APIRateLimit(

            api_key_id=created.id,

            requests_per_minute=

                limits["requests_per_minute"],


            requests_per_day=

                limits["requests_per_day"],


            requests_per_month=

                limits["requests_per_month"]

        )





        self.api_rate_limit_repository.create(

            db,

            rate_limit

        )

        self.audit_service.log_event(

            db,

            action="API_KEY_CREATED",

            description=f"API Key created: {name}",

            organization_id=organization_id

        )



        return {


            "id":

                created.id,


            "api_key":

                raw_key,


            "status":

                created.status

        }





    # =====================================================
    # Authenticate API Key
    # =====================================================


    def authenticate_api_key(

        self,

        db: Session,

        api_key_value: str

    ):


        key_hash = hashlib.sha256(

            api_key_value.encode()

        ).hexdigest()





        api_key = self.api_key_repository.get_by_hash(

            db,

            key_hash

        )





        if not api_key:

            return None





        if api_key.status != "active":

            return None





        self.api_key_repository.update_last_used(

            db,

            api_key

        )





        return api_key



    # =====================================================
    # Validate Subscription Access
    # =====================================================


    def check_subscription_access(

        self,

        db: Session,

        api_key: APIKey

    ):


        return self.subscription_guard.check_access(

            db,

            api_key.organization_id

        )

    # =====================================================
    # Record Usage
    # =====================================================


    def record_usage(

        self,

        db: Session,

        api_key: APIKey,

        endpoint: str

    ):


        usage = APIUsage(

            api_key_id=api_key.id,

            endpoint=endpoint,

            requests_count=1

        )



        created_usage = self.api_usage_repository.create(

            db,

            usage

        )


        self.audit_service.log_event(

            db,

            action="API_USAGE_RECORDED",

            description=f"Endpoint accessed: {endpoint}",

            organization_id=api_key.organization_id

        )


        return created_usage




    # =====================================================
    # Check Rate Limit
    # =====================================================


    def check_rate_limit(

        self,

        db: Session,

        api_key: APIKey

    ):


        rate_limit = self.api_rate_limit_repository.get_by_api_key(

            db,

            api_key.id

        )


        if not rate_limit:

            return {

                "allowed": True,

                "limit": None,

                "current": 0

            }



        minute_usage = self.api_usage_repository.get_requests_last_minute(

            db,

            api_key.id

        )


        daily_usage = self.api_usage_repository.get_requests_today(

            db,

            api_key.id

        )


        monthly_usage = self.api_usage_repository.get_requests_this_month(

            db,

            api_key.id

        )



        if minute_usage >= rate_limit.requests_per_minute:

            return {

                "allowed": False,

                "type": "requests_per_minute",

                "reason": "minute_limit",

                "current": minute_usage,

                "limit": rate_limit.requests_per_minute

            }



        if daily_usage >= rate_limit.requests_per_day:

            return {

                "allowed": False,

                "type": "requests_per_day",

                "reason": "daily_limit",

                "current": daily_usage,

                "limit": rate_limit.requests_per_day

            }



        if monthly_usage >= rate_limit.requests_per_month:

            return {

                "allowed": False,

                "type": "requests_per_month",

                "reason": "monthly_limit",

                "current": monthly_usage,

                "limit": rate_limit.requests_per_month

            }



        return {

            "allowed": True,

            "usage": {

                "minute": minute_usage,

                "day": daily_usage,

                "month": monthly_usage

            },

            "limits": {

                "minute": rate_limit.requests_per_minute,

                "day": rate_limit.requests_per_day,

                "month": rate_limit.requests_per_month

            }

        }