from enum import Enum


class Entitlement(str, Enum):
    EXPIRED = "EXPIRED"
    FREE = "FREE"
    PAID = "PAID"
    PARTNER = "PARTNER"
    PROFESSIONAL = "PROFESSIONAL"
    STUDIO = "STUDIO"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
