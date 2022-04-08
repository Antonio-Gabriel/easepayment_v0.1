from abc import ABC, abstractmethod


class IWalletRepository(ABC):
    @abstractmethod
    def deposit(amount: float, user_id: str):
        """Deposit balance in account"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def with_draw(amount: float, user_id: str):
        """WithDraw balance in account"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def initialize(user_id: str):
        """Initialize wallet"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(user_id: str):
        """Get state of wallet"""

        raise NotImplementedError("Method not implemented")
