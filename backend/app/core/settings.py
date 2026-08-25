import os
from pathlib import Path


class Settings:
    """
    ASEO Application Settings
    Central configuration layer
    """

    APP_NAME = "ASEO Platform"

    VERSION = "23.0.0"

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "false"
    ).lower() == "true"


    # =========================
    # Security
    # =========================

    SECRET_KEY = os.getenv(
        "SECRET_KEY"
    )

    if not SECRET_KEY and ENVIRONMENT == "production":

        raise RuntimeError(
            "SECRET_KEY is required in production"
        )


    JWT_ALGORITHM = os.getenv(
        "JWT_ALGORITHM",
        "HS256"
    )


    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            "60"
        )
    )


    # =========================
    # Database
    # =========================

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )


    # =========================
    # CORS
    # =========================

    CORS_ORIGINS = [

        origin.strip()

        for origin in os.getenv(
            "CORS_ORIGINS",
            "http://localhost:3000"
        ).split(",")

    ]


    # =========================
    # Paths
    # =========================

    BASE_DIR = Path(__file__).resolve().parent.parent.parent



settings = Settings()