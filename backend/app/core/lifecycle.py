from contextlib import asynccontextmanager

from sqlalchemy import text

from fastapi import FastAPI

from app.database.session import (
    get_database
)





@asynccontextmanager
async def lifespan(
    app: FastAPI
):

    """
    ASEO Application Lifecycle Manager

    Handles:

    - Startup initialization
    - Database health check
    - Shutdown cleanup

    """



    # ==========================
    # STARTUP
    # ==========================


    print(
        "🚀 ASEO Application Starting..."
    )


    db = None


    try:


        db = next(
            get_database()
        )


        db.execute(
             text("SELECT 1")
        )


        print(
            "✅ Database connection verified"
        )



    except Exception as error:


        print(

            "❌ Database startup check failed:",

            error

        )



    finally:


        if db:

            db.close()



    print(
        "✅ ASEO Startup Completed"
    )



    yield



    # ==========================
    # SHUTDOWN
    # ==========================


    print(
        "🛑 ASEO Application Shutting Down..."
    )


    # Future cleanup:

    # - Redis connections
    # - Background workers
    # - AI Engine state
    # - Memory flush



    print(
        "✅ ASEO Shutdown Completed"
    )