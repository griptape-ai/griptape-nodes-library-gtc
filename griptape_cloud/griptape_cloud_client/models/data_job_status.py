from enum import Enum


class DataJobStatus(str, Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
