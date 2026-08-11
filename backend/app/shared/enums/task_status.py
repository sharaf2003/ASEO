from enum import Enum


class TaskStatus(str, Enum):
    """
    Lifecycle states for ASEO tasks.
    """

    PENDING = "PENDING"

    RUNNING = "RUNNING"

    SUCCESS = "SUCCESS"

    FAILED = "FAILED"