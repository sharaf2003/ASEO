from fastapi import FastAPI
from sqlalchemy import text

# ==========================
# API Routers
# ==========================

from app.api import (
    projects,
    executions,
    dashboard,
    metrics,
    organizations,
    workspaces,
    users,
    auth,
    project_members,
    project_invitations,
)

# ==========================
# Database Health
# ==========================

from app.database.connection import SessionLocal


# ==========================
# Application
# ==========================


app = FastAPI(
    title="ASEO Platform",
    description="""
Autonomous Software Engineering Organization.

AI-powered software engineering platform
for autonomous project generation,
analysis, deployment and operations.
""",
    version="23.0.0",
)


# =====================================================
# API ROUTERS
# =====================================================


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
    dashboard.router,
    prefix="/api",
    tags=["Dashboard"],
)


app.include_router(
    metrics.router,
    prefix="/api",
    tags=["Metrics"],
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
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"],
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



# =====================================================
# SYSTEM HEALTH
# =====================================================


@app.get(
    "/health",
    tags=["System"],
    summary="System Health Check",
)
def health_check():

    database_status = "unknown"

    try:

        db = SessionLocal()

        db.execute(
            text("SELECT 1")
        )

        database_status = "connected"

    except Exception:

        database_status = "disconnected"

    finally:

        try:
            db.close()

        except Exception:
            pass


    return {

        "system": "ASEO",

        "status": "running",

        "version": "23.0.0",

        "architecture":
            "Layered Multi-Tenant Architecture",

        "database":
            database_status,

    }



# =====================================================
# SYSTEM INFORMATION
# =====================================================


@app.get(
    "/info",
    tags=["System"],
    summary="System Information",
)
def system_info():

    return {

        "message":
            "Welcome to ASEO Platform",

        "version":
            "23.0.0",

        "architecture":
            "Organization → Workspace → User → Project",

        "docs":
            "/docs",

        "health":
            "/health",

    }