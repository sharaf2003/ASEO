import json
import os



class JsonStore:
    """
    ASEO JSON Persistent Storage v14
    """



    def __init__(
        self,
        file_path
    ):

        self.file_path = file_path


        self._initialize()





    def _initialize(self):

        folder = os.path.dirname(

            self.file_path

        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



        if not os.path.exists(

            self.file_path

        ):

            with open(

                self.file_path,

                "w",

                encoding="utf-8"

            ) as file:

                json.dump(

                    [],

                    file

                )





    def save(
        self,
        data
    ):


        with open(

            self.file_path,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                data,

                file,

                indent=4,

                ensure_ascii=False

            )





    def load(self):


        with open(

            self.file_path,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(file)