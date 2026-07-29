import os

from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

from jose import JWTError, jwt





# ==========================
# Load Environment Variables
# ==========================

load_dotenv()





# ==========================
# JWT Configuration
# ==========================


SECRET_KEY = os.getenv(

    "SECRET_KEY"

)


ALGORITHM = os.getenv(

    "JWT_ALGORITHM",

    "HS256"

)


ACCESS_TOKEN_EXPIRE_MINUTES = int(

    os.getenv(

        "ACCESS_TOKEN_EXPIRE_MINUTES",

        "60"

    )

)





# ==========================
# Create Token
# ==========================


def create_access_token(

    data: dict

):


    to_encode = data.copy()



    expire = datetime.now(

        timezone.utc

    ) + timedelta(

        minutes=ACCESS_TOKEN_EXPIRE_MINUTES

    )



    to_encode.update({

        "exp": expire

    })



    return jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM

    )





# ==========================
# Decode Token
# ==========================


def decode_access_token(

    token: str

):


    try:


        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )


        return payload



    except JWTError:


        return None