from enum import Enum


class EnvVarSource(str, Enum):
    MANUAL = "manual"
    SECRET_REF = "secret_ref"

    def __str__(self) -> str:
        return str(self.value)
