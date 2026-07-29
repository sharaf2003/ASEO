from ai_engine.intelligence.prompts import (
    Prompt,
    PromptManager
)



manager = PromptManager()



manager.register(

    Prompt(

        "architecture",

        "Design {framework} backend architecture"

    )

)



result = manager.render(

    "architecture",

    framework="FastAPI"

)



print(result)