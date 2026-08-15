from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


from app.shared.enums.execution_status import ExecutionStatus
from app.shared.enums.task_status import TaskStatus

from app.shared.models.task import Task
from app.shared.models.artifact import Artifact



@dataclass
class ExecutionContext:

    """
    Domain execution context for ASEO engine.

    Represents a running autonomous
    software engineering execution.
    """


    id: int | None = None

    project_id: int | None = None

    organization_id: int | None = None


    status: ExecutionStatus = (
        ExecutionStatus.PENDING
    )


    current_agent: str | None = None


    tasks: list[Task] = field(
        default_factory=list
    )


    artifacts: list[Artifact] = field(
        default_factory=list
    )


    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    started_at: datetime | None = None

    finished_at: datetime | None = None



    # =====================================================
    # Execution Lifecycle
    # =====================================================


    def start(
        self,
        agent_name: str | None = None
    ):

        """
        Start execution.
        """

        self.status = ExecutionStatus.RUNNING

        self.current_agent = agent_name

        self.started_at = datetime.utcnow()



    def complete(self):

        """
        Mark execution as completed.
        """

        self.status = ExecutionStatus.SUCCESS

        self.finished_at = datetime.utcnow()



    def fail(
        self,
        reason: str
    ):

        """
        Mark execution as failed.
        """

        self.status = ExecutionStatus.FAILED

        self.metadata["error"] = reason

        self.finished_at = datetime.utcnow()



    # =====================================================
    # Task Management
    # =====================================================


    def create_task(

        self,

        name: str,

        agent_name: str,

        description: str | None = None

    ) -> Task:

        """
        Create and attach a new execution task.
        """


        task = Task(

            name=name,

            agent_name=agent_name,

            description=description,

            status=TaskStatus.PENDING

        )


        self.add_task(task)


        return task



    def start_task(

        self,

        task: Task

    ):

        """
        Move task to running state.
        """

        task.start()



    def complete_task(

        self,

        task: Task,

        output: dict[str, Any] | None = None

    ):

        """
        Mark task as completed.
        """

        task.status = TaskStatus.COMPLETED

        if output:

            task.output_data = output


        task.completed_at = datetime.utcnow()



    def fail_task(

        self,

        task: Task,

        error: str

    ):

        """
        Mark task as failed.
        """

        task.fail(error)



    # =====================================================
    # Task / Artifact Registration
    # =====================================================


    def add_task(

        self,

        task: Task

    ):

        """
        Attach task to execution.
        """


        task.execution_id = self.id

        self.tasks.append(task)



    def add_artifact(

        self,

        artifact: Artifact

    ):

        """
        Attach artifact to execution.
        """


        artifact.execution_id = self.id

        self.artifacts.append(artifact)