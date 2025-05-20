from enum import Enum


class InviteResponseStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
