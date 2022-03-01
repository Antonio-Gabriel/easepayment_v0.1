from abc import ABC, abstractmethod
from ..domain.entityprops import AccountProps


class IAccountRepository(ABC):
    @abstractmethod
    def save(account: AccountProps, id: str):
        """Save account into db"""

        raise NotImplementedError("Method not implemented")
