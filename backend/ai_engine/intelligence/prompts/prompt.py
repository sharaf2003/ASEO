from dataclasses import dataclass



@dataclass
class Prompt:

    """
    ASEO Prompt Object v13
    """

    name: str

    template: str



    def render(
        self,
        **kwargs
    ):

        return self.template.format(
            **kwargs
        )