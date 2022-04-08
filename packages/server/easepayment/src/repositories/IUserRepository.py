from abc import ABC, abstractmethod
from ..domain.entityprops import UserProps


class IUserRepository(ABC):
    @abstractmethod
    def save(user: UserProps):
        """Save user into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def remove(user_id: str):
        """remove user into db"""

        raise NotImplementedError("Method not implemented")
