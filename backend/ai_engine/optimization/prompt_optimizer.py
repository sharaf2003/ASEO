from .prompt_variant import PromptVariant




class PromptOptimizer:
    """
    ASEO Prompt Optimization Engine v14
    """



    def __init__(self):

        self.variants = []





    def optimize(
        self,
        prompt,
        feedback=None
    ):


        optimized = prompt



        if "backend" in prompt.lower():

            optimized = (

                prompt

                +

                " with scalable architecture, "

                "security best practices, "

                "and clean code principles."

            )



        if feedback:

            optimized += (

                " Improve based on: "

                +

                feedback

            )




        variant = PromptVariant(

            prompt,

            optimized,

            100

        )



        self.variants.append(

            variant

        )


        return variant.to_dict()





    def history(self):


        return [

            item.to_dict()

            for item

            in self.variants

        ]