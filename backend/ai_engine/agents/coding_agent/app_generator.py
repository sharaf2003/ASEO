class AppGenerator:
    """
    ASEO FastAPI Application Generator v1
    """



    def generate(
        self
    ):


        return """

from fastapi import FastAPI



app = FastAPI()



@app.get("/")

def home():

    return {

        "message":

        "ASEO Generated API"

    }

"""