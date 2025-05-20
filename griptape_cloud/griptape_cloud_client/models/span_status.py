from enum import Enum


class SpanStatus(str, Enum):
    ERROR = "ERROR"
    OK = "OK"
    UNSET = "UNSET"

    def __str__(self) -> str:
        return str(self.value)
