from fastapi.testclient import TestClient

from ai_engine.api_gateway import (
    ASEOGateway
)



gateway = ASEOGateway()


client = TestClient(

    gateway.get_app()

)



register = client.post(

    "/auth/register",

    params={

        "email":
        "owner@startup.com",

        "password":
        "123456"

    }

)



login = client.post(

    "/auth/login",

    params={

        "email":
        "owner@startup.com",

        "password":
        "123456"

    }

)



project = client.post(

    "/projects/create",

    params={

        "name":
        "Ecommerce Platform"

    }

)



projects = client.get(

    "/projects/all"

)



print({

    "register":
        register.json(),

    "login":
        login.json(),

    "project":
        project.json(),

    "projects":
        projects.json()

})