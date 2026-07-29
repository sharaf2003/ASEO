class TaskGenerator:
    """
    ASEO Task Generator v1

    Generates tasks from phases.

    """



    def generate(
        self,
        phase
    ):


        return phase.get(
            "tasks",
            []
        )