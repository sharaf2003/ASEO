class SchemaGenerator:
    """
    ASEO Schema Generator v1
    """



    def generate(
        self,
        entity
    ):


        class_name = entity.capitalize()



        return f"""

from pydantic import BaseModel



class {class_name}Create(BaseModel):

    pass



class {class_name}Response(BaseModel):

    id: int

"""