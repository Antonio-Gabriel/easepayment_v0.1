from abc import ABC, abstractmethod


class IUniformRepository(ABC):
    @abstractmethod
    def pay_uniform(id: str, uniform_type_id: str, payment_id: str):
        """Pay uniform"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def save_uniform_type(id: str, type: str, price: float):
        """Save uniform type"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_uniform_type():
        """Uniform type"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_uniform_payed(user_id: str):
        """Get uniform payed"""

        raise NotImplementedError("Method not implemented")
