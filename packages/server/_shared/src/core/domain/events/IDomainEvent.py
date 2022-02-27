from abc import ABC, abstractmethod
from typing import Type


class IDomainEvent(ABC):
    """Usecase interface"""

    @abstractmethod
    def dispatch(event: Type[any]) -> int:
        raise NotImplementedError("Method not implemented")
