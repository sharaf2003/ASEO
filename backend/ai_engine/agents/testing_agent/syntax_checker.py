import ast



class SyntaxChecker:
    """
    ASEO Python Syntax Checker v1
    """



    def check(
        self,
        file_path
    ):


        try:


            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:


                code = file.read()



            ast.parse(
                code
            )



            return {


                "file":

                    file_path,


                "status":

                    "passed",


                "error":

                    None

            }



        except Exception as error:


            return {


                "file":

                    file_path,


                "status":

                    "failed",


                "error":

                    str(error)

            }