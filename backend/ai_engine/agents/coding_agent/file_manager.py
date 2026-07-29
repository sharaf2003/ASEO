import os



class FileManager:
    """
    ASEO File Manager v1
    """



    def create_directory(
        self,
        path
    ):


        os.makedirs(
            path,
            exist_ok=True
        )





    def create_file(
        self,
        path,
        content
    ):


        directory = os.path.dirname(
            path
        )


        if directory:

            self.create_directory(
                directory
            )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:


            file.write(
                content
            )