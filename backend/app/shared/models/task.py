from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from app.shared.enums.task_status import TaskStatus


@dataclass
class Task:
    """
    Domain representation of an ASEO execution task.

    A task represents a unit of work assigned
    to an autonomous agent.
    """

    id: int | None = None

    name: str = ""

    description: str = ""

    agent_name: str = ""

    status: TaskStatus = TaskStatus.PENDING

    input_data: dict[str, Any] = field(
        default_factory=dict
    )

    output_data: dict[str, Any] = field(
        default_factory=dict
    )

    execution_id: int | None = None

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    completed_at: datetime | None = None


    def start(self):
        """
        Move task into execution state.
        """

        self.status = TaskStatus.RUNNING



    def complete(
        self,
        output: dict[str, Any] | None = None
    ):
        """
        Mark task as completed.
        """

        self.status = TaskStatus.SUCCESS

        if output:

            self.output_data = output


        self.completed_at = datetime.utcnow()



    def fail(
        self,
        error: str
    ):
        """
        Mark task as failed.
        """

        self.status = TaskStatus.FAILED

        self.output_data = {

            "error": error

        }

        self.completed_at = datetime.utcnow()