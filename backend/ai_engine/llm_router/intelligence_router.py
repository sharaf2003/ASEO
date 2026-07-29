from .task_router import (
    TaskRouter
)

from .model_registry import (
    ModelRegistry
)



class IntelligenceRouter:
    """
    ASEO LLM Intelligence Router v16
    """



    def __init__(
        self
    ):


        self.task_router = TaskRouter()


        self.registry = ModelRegistry()





    def select_model(
        self,
        task
    ):


        category = self.task_router.classify(

            task

        )


        model = self.registry.get_model(

            category

        )



        return {


            "task":

                category,


            "selected_model":

                model,


            "reason":

                f"{category} task requires {model}"

        }