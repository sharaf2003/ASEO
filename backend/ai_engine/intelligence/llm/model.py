from dataclasses import dataclass



@dataclass
class LLMRequest:
    """
    ASEO LLM Request v13
    """

    prompt: str

    system: str = ""

    temperature: float = 0.7





@dataclass
class LLMResponse:
    """
    ASEO LLM Response v13
    """

    content: str

    model: str

    tokens: int = 0