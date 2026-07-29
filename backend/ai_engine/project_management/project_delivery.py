from .sprint_manager import SprintManager

from .task_planner import TaskPlanner

from .delivery_tracker import DeliveryTracker




class ProjectDelivery:
    """
    ASEO Autonomous Project Delivery v22.0
    """

    def __init__(self):

        self.sprint = SprintManager()

        self.planner = TaskPlanner()

        self.tracker = DeliveryTracker()



    def deliver(
        self,
        product
    ):


        sprint = self.sprint.create_sprint(

            product

        )


        tasks = self.planner.create_tasks(

            product

        )


        delivery = self.tracker.track(

            tasks

        )


        return {

            "sprint":
                sprint,

            "tasks":
                tasks,

            "delivery":
                delivery,

            "status":
                "completed"

        }