class ExecutionMonitor:
    """
    ASEO Execution Monitor v22.1
    """

    def monitor(
        self,
        results
    ):


        completed = len(

            [

                r for r in results

                if r["status"] == "completed"

            ]

        )


        return {

            "total":
                len(results),

            "completed":
                completed,

            "success_rate":
                (completed / len(results)) * 100
                if results else 0,

            "status":
                "healthy"

        }