from .prompt import Prompt




class PromptManager:
    """
    ASEO Prompt Manager v13
    """



    def __init__(self):

        self.prompts = {}





    def register(
        self,
        prompt: Prompt
    ):


        self.prompts[

            prompt.name

        ] = prompt





    def get(
        self,
        name
    ):


        return self.prompts.get(

            name

        )




    def render(
        self,
        name,
        **kwargs
    ):


        prompt = self.get(name)



        if not prompt:

            raise Exception(
                "Prompt not found"
            )



        return prompt.render(

            **kwargs

        )