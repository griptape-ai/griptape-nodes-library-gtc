from enum import Enum


class IntegrationType(str, Enum):
    GITHUB_APP = "github_app"
    SLACK = "slack"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
