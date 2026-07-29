from sqlalchemy.orm import Session

from app.database.connection import SessionLocal





def get_database():

    """
    Database dependency injection
    for FastAPI routes.
    """

    db: Session = SessionLocal()


    try:

        yield db


    finally:

        db.close()