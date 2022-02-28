from abc import ABC, abstractmethod


class IPayment(ABC):
    @abstractmethod
    def payment_role(*args, **kwargs):
        """Rule from pay"""

        raise NotImplementedError("Method not implemented")
