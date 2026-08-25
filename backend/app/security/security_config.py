"""
ASEO Production Security Configuration.
"""


from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.middleware.security_headers import (
    SecurityHeadersMiddleware
)




class SecurityConfig:

    """
    Production security settings.
    """



    ALLOWED_HOSTS = [

        "localhost",

        "127.0.0.1",

    ]



    ALLOWED_ORIGINS = [

        "http://localhost:3000",

        "http://localhost:5173",

    ]





def add_security_middleware(app):

    """
    Register production security middleware.
    """

    app.add_middleware(
        SecurityHeadersMiddleware
    )
    

    app.add_middleware(

        TrustedHostMiddleware,

        allowed_hosts=SecurityConfig.ALLOWED_HOSTS

    )



    app.add_middleware(

        CORSMiddleware,

        allow_origins=SecurityConfig.ALLOWED_ORIGINS,

        allow_credentials=True,

        allow_methods=[

            "*"

        ],

        allow_headers=[

            "*"

        ]

    )