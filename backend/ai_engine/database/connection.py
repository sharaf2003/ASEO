import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_USER = os.getenv(
    "DATABASE_USER",
    "aseo"
)

DATABASE_PASSWORD = os.getenv(
    "DATABASE_PASSWORD",
    "aseo_password"
)

DATABASE_HOST = os.getenv(
    "DATABASE_HOST",
    "localhost"
)

DATABASE_PORT = os.getenv(
    "DATABASE_PORT",
    "5433"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "aseo_db"
)


DATABASE_URL = (
    f"postgresql://"
    f"{DATABASE_USER}:"
    f"{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:"
    f"{DATABASE_PORT}/"
    f"{DATABASE_NAME}"
)



engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True

)



SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)



def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()