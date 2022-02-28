from abc import ABC, abstractmethod


class IPaymentRepo(ABC):
    @abstractmethod
    def findByPaymentIdAndMonth(payment_id: str, month: str):
        """Find payment and month"""

        raise NotImplementedError("Method not implemented")
