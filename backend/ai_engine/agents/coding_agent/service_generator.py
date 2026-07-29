class ServiceGenerator:
    """
    ASEO Service Generator v1
    """



    def generate(
        self,
        entity
    ):


        return f"""

class {entity.capitalize()}Service:



    def get_all(self):

        return []



    def create(self, data):

        return data

"""