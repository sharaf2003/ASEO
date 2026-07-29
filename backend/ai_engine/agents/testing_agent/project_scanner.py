import os



class ProjectScanner:
    """
    ASEO Project Scanner v1
    """



    def scan(
        self,
        path
    ):


        files = []



        for root, dirs, filenames in os.walk(path):


            for file in filenames:


                if file.endswith(".py"):


                    files.append(

                        os.path.join(
                            root,
                            file
                        )

                    )



        return files