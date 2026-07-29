class CodingIntelligence:

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
            prompt
        )

        return {
            "decision": decision.to_dict(),
            "response": response.content
        }