class FailureAnalyzer:


    """
    Analyzes failed executions
    and extracts improvement signals.
    """


    def analyze(

        self,

        execution_result: dict,

        architecture_decisions: list

    ) -> dict:


        failures = []


        if not execution_result:

            return {

                "failed": False,

                "failures": []

            }



        success = execution_result.get(

            "success",

            True

        )



        if success:

            return {

                "failed": False,

                "failures": []

            }



        for decision in architecture_decisions:


            failures.append({

                "pattern_id": decision.get(

                    "id"

                ),

                "pattern": decision.get(

                    "pattern"

                ),

                "layer": decision.get(

                    "layer"

                ),

                "reason":

                    "Pattern involved in failed execution"

            })



        return {


            "failed": True,


            "failures": failures

        }