from abc import ABC, abstractmethod
from ..domain.entityprops import OwnerProps


class IOwnerRepository(ABC):
    @abstractmethod
    def find_by_email(email: str):
        """Find owner by email"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_by_phone(phone: str):
        """Find owner by phone number"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def save(owner_props: OwnerProps):
        """Save owner into db"""

        raise NotImplementedError("Method not implemented")
