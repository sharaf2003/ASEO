import json
import os



class ExperienceStore:
    """
    ASEO Persistent Experience Store v16.8.2

    Persistent Engineering Memory Storage
    """



    def __init__(
        self,
        file_path="engineering_memory.json"
    ):


        self.file_path = file_path


        self.memories = []


        self.load()





    def load(
        self
    ):


        if os.path.exists(
            self.file_path
        ):


            try:

                with open(
                    self.file_path,
                    "r",
                    encoding="utf-8"
                ) as file:


                    self.memories = json.load(
                        file
                    )


            except Exception:


                self.memories = []



        else:


            self.memories = []







    def save(
        self,
        memory
    ):


        self.memories.append(

            memory

        )


        self.persist()


        return memory







    def persist(
        self
    ):


        with open(

            self.file_path,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                self.memories,

                file,

                indent=4,

                ensure_ascii=False

            )







    def all(
        self
    ):


        return self.memories