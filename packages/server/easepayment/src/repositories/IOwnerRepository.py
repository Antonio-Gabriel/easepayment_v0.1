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
    def get():
        """get all owners"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(owner_id: str):
        """get owner by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def save(owner_props: OwnerProps):
        """Save owner into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def update(owner_props: OwnerProps):
        """update owner into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(owner_id: str):
        """delete owner into db"""

        raise NotImplementedError("Method not implemented")
