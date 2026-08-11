from enum import Enum


class ExecutionStatus(str, Enum):
    """
    Unified execution status across the ASEO platform.
    """

    SUCCESS = "success"
    FAILED = "failed"
    RETRY = "retry"
    SKIPPED = "skipped"
    CANCELLED = "cancelled"
    RUNNING = "running"
    PENDING = "pending"