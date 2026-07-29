from .engineering_plan import (
    EngineeringPlan
)



class EngineeringAnalyzer:
    """
    ASEO Engineering Analyzer v16
    """



    def analyze(
        self,
        requirement
    ):


        plan = EngineeringPlan(

            requirement

        )


        text = requirement.lower()



        if "ecommerce" in text or "shop" in text:

            plan.domain = "ecommerce"


            plan.complexity = "medium"


            plan.risks = [

                "authentication",

                "database_scaling",

                "payment_security"

            ]


        elif "bank" in text:

            plan.domain = "banking"


            plan.complexity = "high"


            plan.risks = [

                "security",

                "compliance",

                "audit"

            ]


        else:

            plan.domain = "general"


            plan.complexity = "medium"


            plan.risks = [

                "architecture",

                "scalability"

            ]



        return plan.to_dict()