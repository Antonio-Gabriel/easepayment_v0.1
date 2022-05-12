from abc import ABC, abstractmethod


class IMonthlyRepository(ABC):
    @abstractmethod
    def pay_month(id: str, pay_id: str, month: str):
        """Save monthly"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_montly_payed(user_id: str, month: str):
        """Find monthly payed"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_monthly_payed(user_id: str):
        """Get monthly payed"""

        raise NotImplementedError("Method not implemented")
