from abc import ABC, abstractmethod
from typing import Type

from packages.server.easepayment.src.domain.interfaces import IPayment


class IDomainEvent(ABC):
    """Usecase interface"""

    @abstractmethod
    def dispatch(event: Type[any], payment_type: Type[IPayment]) -> int:
        raise NotImplementedError("Method not implemented")
