class TemplateEngine:
    """
    ASEO Template Engine v1
    """



    def render(
        self,
        template,
        variables
    ):


        result = template



        for key, value in variables.items():


            result = result.replace(

                "{{" + key + "}}",

                str(value)

            )



        return result