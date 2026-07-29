from ai_engine.intelligence.reasoning import (
    ReasoningEngine
)

from ai_engine.intelligence.prompts import (
    Prompt,
    PromptManager
)

from ai_engine.intelligence.llm import (
    MockLLMProvider,
    LLMRequest
)



class CodingIntelligence:
    """
    ASEO Coding Intelligence v13
    """


    def __init__(
        self,
        reasoning,
        prompts,
        llm
    ):

        self.reasoning = reasoning
        self.prompts = prompts
        self.llm = llm



    def analyze_project(
        self,
        requirement
    ):


        decision = self.reasoning.analyze(
            requirement
        )


        prompt = self.prompts.render(
            "architecture",
            framework="FastAPI"
        )


        response = self.llm.generate(

            LLMRequest(

                prompt=prompt

            )

        )


        return {

            "decision":
                decision.to_dict(),


            "llm_response":
                response.content

        }





reasoning = ReasoningEngine()


prompts = PromptManager()


prompts.register(

    Prompt(

        "architecture",

        "Design {framework} backend architecture"

    )

)



llm = MockLLMProvider()



coding_ai = CodingIntelligence(

    reasoning,

    prompts,

    llm

)



result = coding_ai.analyze_project(

    "Build ecommerce backend system"

)



print(result)