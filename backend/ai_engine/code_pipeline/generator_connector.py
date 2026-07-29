class GeneratorConnector:
    """
    ASEO Code Generator Connector v17.3
    """



    def __init__(
        self
    ):

        self.generator = "code_generator"





    def generate(
        self,
        project
    ):


        files = [

            f"{project}/main.py",

            f"{project}/database.py",

            f"{project}/routes/users.py",

            f"{project}/routes/products.py",

            f"{project}/routes/orders.py"

        ]



        return {


            "project":

                project,


            "files":

                files,


            "generated":

                True

        }