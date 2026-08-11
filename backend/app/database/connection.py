"""
ASEO Database Connection Layer

Responsible for:
- PostgreSQL engine creation
- Connection pooling
- Session management
"""

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()


# =====================================================
# DATABASE CONFIGURATION
# =====================================================


DATABASE_USER = os.getenv(
    "DATABASE_USER",
    "aseo",
)


DATABASE_PASSWORD = quote_plus(
    os.getenv(
        "DATABASE_PASSWORD",
        "aseo_password",
    )
)


DATABASE_HOST = os.getenv(
    "DATABASE_HOST",
    "127.0.0.1",
)


DATABASE_PORT = os.getenv(
    "DATABASE_PORT",
    "5432",
)


DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "aseo_db",
)



DATABASE_URL = (
    f"postgresql://{DATABASE_USER}:"
    f"{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:"
    f"{DATABASE_PORT}/"
    f"{DATABASE_NAME}"
)



# =====================================================
# DATABASE ENGINE
# =====================================================


engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True,

    pool_recycle=300,

    pool_size=10,

    max_overflow=20,

    pool_timeout=30,

    echo=False,

)



# =====================================================
# DATABASE SESSION
# =====================================================


SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine,

)