from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from app.shared.enums.execution_status import ExecutionStatus

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



    def start(self, agent_name: str | None = None):
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



    def fail(self, reason: str):
        """
        Mark execution as failed.
        """

        self.status = ExecutionStatus.FAILED

        self.metadata["error"] = reason

        self.finished_at = datetime.utcnow()



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