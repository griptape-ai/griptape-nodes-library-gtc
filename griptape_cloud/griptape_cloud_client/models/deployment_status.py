from enum import Enum


class DeploymentStatus(str, Enum):
    DEPLOYING = "DEPLOYING"
    ERROR = "ERROR"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
