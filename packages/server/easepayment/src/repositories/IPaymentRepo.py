from abc import ABC, abstractmethod


class IPaymentRepo(ABC):
    @abstractmethod
    def pay(user_id: str, student_id: str, amount: float, pay_id: str):
        """Pay"""

        raise NotImplementedError("Method not implemented")
