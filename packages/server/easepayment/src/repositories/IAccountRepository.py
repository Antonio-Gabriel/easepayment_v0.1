from abc import ABC, abstractmethod
from ..domain.entityprops import AccountProps


class IAccountRepository(ABC):
    @abstractmethod
    def save(account_props: AccountProps):
        """Save account into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_by_id(account_id: str):
        """Find account by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def update(account_props: AccountProps):
        """Update account"""

        raise NotImplementedError("Method not implemented")
