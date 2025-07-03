from enum import Enum


class CreditTransactionType(str, Enum):
    DEBIT = "DEBIT"
    GRANT = "GRANT"

    def __str__(self) -> str:
        return str(self.value)
