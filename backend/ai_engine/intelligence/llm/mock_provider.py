from .provider import LLMProvider

from .model import (
    LLMRequest,
    LLMResponse
)



class MockLLMProvider(LLMProvider):
    """
    ASEO Mock LLM Provider v13

    Used for testing intelligence layer.
    """



    def generate(
        self,
        request: LLMRequest
    ):


        return LLMResponse(

            content=
                f"AI Response: {request.prompt}",


            model=
                "ASEO-Mock-LLM",


            tokens=
                len(request.prompt.split())

        )