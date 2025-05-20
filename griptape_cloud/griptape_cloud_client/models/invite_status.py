from enum import Enum


class InviteStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    EXPIRED = "EXPIRED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
