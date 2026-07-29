from abc import ABC, abstractmethod

from .model import (
    LLMRequest,
    LLMResponse
)




class LLMProvider(ABC):
    """
    ASEO LLM Provider Interface v13
    """



    @abstractmethod
    def generate(
        self,
        request: LLMRequest
    ) -> LLMResponse:

        pass