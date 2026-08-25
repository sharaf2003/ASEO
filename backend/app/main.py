from fastapi import FastAPI

from app.core.settings import settings

from app.core.middleware import (
    setup_middleware
)

from app.core.exceptions import (
    ASEOException,
    aseo_exception_handler,
    global_exception_handler
)

from app.core.lifecycle import (
    lifespan
)

from app.security.security_config import (
    add_security_middleware
)


# =====================================================
# API ROUTERS
# =====================================================

from app.api import (
    auth,
    organizations,
    workspaces,
    users,
    projects,
    executions,
    dashboard,
    platform_dashboard,
    metrics,
    project_members,
    project_invitations,
    api_keys,
    subscriptions,
    billing,
    billing_dashboard,
    payments,
    payment_webhook,
    audit,
    health
)


from app.middleware.api_gateway_middleware import (
    APIGatewayMiddleware
)


from app.core.logging_config import (
    setup_logging
)


# =====================================================
# APPLICATION
# =====================================================


app = FastAPI(

    title=settings.APP_NAME,

    description="""
Autonomous Software Engineering Organization.

AI-powered software engineering platform
for autonomous project generation,
analysis, deployment and operations.
""",

    version=settings.VERSION,

    lifespan=lifespan

)


# =====================================================
# MIDDLEWARE
# =====================================================


add_security_middleware(app)

setup_middleware(app)

setup_logging()


# =====================================================
# EXCEPTION HANDLERS
# =====================================================


app.add_exception_handler(

    ASEOException,

    aseo_exception_handler

)


app.add_exception_handler(

    Exception,

    global_exception_handler

)


# =====================================================
# ROUTERS
# =====================================================


app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"],
)


app.include_router(
    organizations.router,
    prefix="/api/organizations",
    tags=["Organizations"],
)


app.include_router(
    workspaces.router,
    prefix="/api/workspaces",
    tags=["Workspaces"],
)


app.include_router(
    users.router,
    prefix="/api/users",
    tags=["Users"],
)


app.include_router(
    projects.router,
    prefix="/api/projects",
    tags=["Projects"],
)


app.include_router(
    executions.router,
    prefix="/api",
    tags=["Executions"],
)


app.include_router(
    project_members.router,
    prefix="/api",
    tags=["Project Members"],
)


app.include_router(
    project_invitations.router,
    prefix="/api",
    tags=["Project Invitations"],
)


app.include_router(
    dashboard.router,
    prefix="/api",
    tags=["Dashboard"],
)


app.include_router(
    platform_dashboard.router,
    prefix="/api",
    tags=["Platform Dashboard"],
)


app.include_router(
    metrics.router,
    prefix="/api",
    tags=["Metrics"],
)


app.include_router(
    api_keys.router,
    prefix="/api/api-keys",
    tags=["API Keys"],
)


app.include_router(
    subscriptions.router,
    prefix="/api/subscriptions",
    tags=["Subscriptions"],
)


app.include_router(
    billing.router,
    prefix="/api/billing",
    tags=["Billing"],
)


app.include_router(
    billing_dashboard.router,
    prefix="/api/billing",
    tags=["Billing Dashboard"],
)


app.include_router(
    payments.router,
    prefix="/api/payments",
    tags=["Payments"]
)


app.include_router(
    payment_webhook.router,
    prefix="/api/payments",
    tags=["Payment Webhook"]
)


app.add_middleware(
    APIGatewayMiddleware
)


app.include_router(

    audit.router,

    prefix="/audit",

    tags=["Audit"]

)


# =====================================================
# SYSTEM INFORMATION
# =====================================================
# Health + Metrics
# يحتوي الآن على:
# /health
# /metrics

app.include_router(

    health.router

)

@app.get(
    "/info",
    tags=["System"],
    summary="System Information"
)
def system_info():

    return {

        "message":

            "Welcome to ASEO Platform",


        "version":

            settings.VERSION,


        "architecture":

            "Organization → Workspace → User → Project",


        "docs":

            "/docs",


        "health":

            "/health",

    }