from typing import Type
from abc import ABC, abstractmethod


class IPayment(ABC):
    @abstractmethod
    def payment_role(*args, **kwargs):
        """Rule from pay"""

        raise NotImplementedError("Method not implemented")


class IDomainEvents(ABC):
    """Usecase interface"""

    @abstractmethod
    def dispatch(event: Type[any], payment_type: Type[IPayment]):
        """Dispatch event"""

        raise NotImplementedError("Method not implemented")
