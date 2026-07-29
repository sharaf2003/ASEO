import json
import os



class PersistentStorage:
    """
    ASEO Persistent Memory Storage v1

    Responsible for:

    - Saving AI knowledge
    - Loading previous knowledge
    - Updating memory storage

    Storage:

    JSON File

    """



    def __init__(
        self,
        file_path="ai_engine/memory/memory.json"
    ):


        self.file_path = file_path



        self.ensure_storage()





    # =====================================
    # Create Storage
    # =====================================

    def ensure_storage(
        self
    ):


        directory = os.path.dirname(
            self.file_path
        )


        if not os.path.exists(directory):

            os.makedirs(
                directory
            )



        if not os.path.exists(
            self.file_path
        ):


            with open(
                self.file_path,
                "w",
                encoding="utf-8"
            ) as file:


                json.dump(
                    {},
                    file,
                    ensure_ascii=False,
                    indent=4
                )





    # =====================================
    # Save Data
    # =====================================

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
                ensure_ascii=False,
                indent=4
            )





    # =====================================
    # Load Data
    # =====================================

    def load(
        self
    ):


        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:


            return json.load(
                file
            )