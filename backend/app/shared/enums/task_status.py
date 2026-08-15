from enum import Enum


class TaskStatus(str, Enum):

    CREATED = "CREATED"

    PENDING = "PENDING"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"
