"""
ASEO Production Logging Configuration.
"""


import logging

import sys

import os

from logging.handlers import RotatingFileHandler





class LoggingConfig:

    """
    Central logging configuration.
    """


    LOG_FORMAT = (

        "%(asctime)s | "

        "%(levelname)s | "

        "%(name)s | "

        "%(message)s"

    )


    LOG_LEVEL = logging.INFO


    LOG_DIR = "logs"


    ERROR_LOG = "logs/errors.log"


    APP_LOG = "logs/app.log"






def setup_logging():

    """
    Configure application logging.
    """


    # Create logs directory if missing

    os.makedirs(

        LoggingConfig.LOG_DIR,

        exist_ok=True

    )




    formatter = logging.Formatter(

        LoggingConfig.LOG_FORMAT

    )




    console_handler = logging.StreamHandler(

        sys.stdout

    )


    console_handler.setFormatter(

        formatter

    )





    app_handler = RotatingFileHandler(

        LoggingConfig.APP_LOG,

        maxBytes=10 * 1024 * 1024,

        backupCount=5

    )


    app_handler.setFormatter(

        formatter

    )





    error_handler = RotatingFileHandler(

        LoggingConfig.ERROR_LOG,

        maxBytes=10 * 1024 * 1024,

        backupCount=5

    )


    error_handler.setLevel(

        logging.ERROR

    )


    error_handler.setFormatter(

        formatter

    )





    logging.basicConfig(

        level=LoggingConfig.LOG_LEVEL,

        handlers=[

            console_handler,

            app_handler,

            error_handler

        ]

    )







def get_logger(name: str):

    """
    Create application logger.
    """


    return logging.getLogger(name)