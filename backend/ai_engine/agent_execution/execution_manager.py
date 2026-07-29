from .task_generator import TaskGenerator

from .agent_dispatcher import AgentDispatcher

from .execution_engine import ExecutionEngine




class ExecutionManager:
    """
    ASEO Execution Manager v21.2
    """



    def __init__(self):

        self.generator = TaskGenerator()

        self.dispatcher = AgentDispatcher()

        self.engine = ExecutionEngine()



    def run(
        self,
        decision
    ):


        task_plan = self.generator.generate(

            decision

        )


        assignments = self.dispatcher.dispatch(

            task_plan["tasks"]

        )


        execution = self.engine.execute(

            assignments

        )


        return {

            "task_plan":
                task_plan,

            "assignments":
                assignments,

            "execution":
                execution

        }