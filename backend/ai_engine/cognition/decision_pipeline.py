class DecisionPipeline:
    """
    ASEO Cognitive Decision Pipeline

    Converts cognitive context
    into a unified engineering decision.
    """



    def create_decision(
        self,
        context
    ):


        action = None

        reasoning = ""

        confidence = context.confidence



        # Extract reasoning safely

        if context.reasoning:


            latest_reasoning = context.reasoning[-1]


            if isinstance(
                latest_reasoning,
                dict
            ):


                action = latest_reasoning.get(

                    "action"

                )


                reasoning = latest_reasoning.get(

                    "reasoning",

                    ""

                )


                confidence = latest_reasoning.get(

                    "confidence",

                    confidence

                )



            elif isinstance(
                latest_reasoning,
                str
            ):


                reasoning = latest_reasoning



        # Ensure valid decision

        if not action:


            action = "No decision generated"



        return {


            # Decision layer

            "action":

                action,


            "reasoning":

                reasoning,


            "confidence":

                confidence,



            # Requirement context

            "requirement":

                context.requirement,



            # Pattern intelligence

            "patterns":

                context.patterns,



            # Evidence fusion

            "evidence":

                context.evidence

        }