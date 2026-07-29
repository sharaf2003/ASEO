from .decision import Decision





class ReasoningEngine:
    """
    ASEO Reasoning Engine v13

    Makes engineering decisions.
    """



    def analyze(
        self,
        requirement
    ):


        requirement = requirement.lower()



        if "ecommerce" in requirement or "shop" in requirement:


            return Decision(

                action="Use FastAPI + PostgreSQL + JWT",

                confidence=0.95,

                reasoning=
                "E-commerce requires scalable API, relational data and authentication."

            )




        return Decision(

            action="Use Layered FastAPI Architecture",

            confidence=0.85,

            reasoning=
            "Default backend architecture decision."

        )