import os



class CodeValidator:
    """
    ASEO Code Validator v1
    """



    def validate_file(
        self,
        path
    ):


        return os.path.exists(
            path
        )