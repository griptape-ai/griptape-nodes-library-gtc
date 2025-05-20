from enum import Enum


class AssistantRunStatus(str, Enum):
    CANCELLED = "CANCELLED"
    ERROR = "ERROR"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    STARTING = "STARTING"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
