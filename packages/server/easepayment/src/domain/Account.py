from packages.server._shared.src.core.domain import Entity
from .validators import PasswordHash
from .entityprops import AccountProps


class Account:
    class __private(Entity[AccountProps]):
        def __init__(self, props: AccountProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: AccountProps, id: str = None):
        """create account object"""

        account = cls.__private(props, id)

        if account.props.password:
            account.props.password = cls.__password_encrypt(account.props.password)

        return account

    @classmethod
    def __password_encrypt(cls, password) -> bytes:
        """Enctrypt password"""

        return PasswordHash.encrypt(password)

    @classmethod
    def compare(cls, hash_pass: str, comparison_pass: bytes) -> bool:
        """Verify if password iblacks valid or not"""

        if hash_pass and comparison_pass:

            return PasswordHash.compare(hash_pass, comparison_pass)

        raise Exception("Do you don't insert password")
