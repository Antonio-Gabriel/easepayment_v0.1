from abc import ABC
from dataclasses import dataclass


@dataclass
class IUseCaseErrorError:
    message: str


class UseCaseError(ABC, IUseCaseErrorError):
    def __init__(self, message: str):
        self.message = message
