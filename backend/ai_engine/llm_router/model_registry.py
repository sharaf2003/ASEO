class ModelRegistry:
    """
    ASEO Model Registry v16
    """



    def __init__(self):

        self.models = {

            "architecture":
                "reasoning-specialist",


            "coding":
                "code-specialist",


            "debugging":
                "debug-specialist",


            "security":
                "security-specialist"

        }





    def get_model(
        self,
        task
    ):


        return self.models.get(

            task,

            "general-model"

        )