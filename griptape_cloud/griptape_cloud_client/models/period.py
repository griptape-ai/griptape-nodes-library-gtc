from enum import Enum


class Period(str, Enum):
    VALUE_0 = "1m"
    VALUE_1 = "1h"
    VALUE_2 = "1d"
    VALUE_3 = "1w"

    def __str__(self) -> str:
        return str(self.value)
