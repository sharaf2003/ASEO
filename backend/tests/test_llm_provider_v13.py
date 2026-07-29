from ai_engine.intelligence.llm import (
    MockLLMProvider,
    LLMRequest
)



provider = MockLLMProvider()



response = provider.generate(

    LLMRequest(

        prompt=
        "Generate FastAPI project architecture"

    )

)



print(
    {
        "content": response.content,
        "model": response.model,
        "tokens": response.tokens
    }
)