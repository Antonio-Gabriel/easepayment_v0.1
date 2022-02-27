from packages.server._shared.src.core.domain import Entity
from packages.server._shared.src.core.logic import Result, Guard

from .validators import PasswordHash
from .entityprops import AccountProps


class Account:
    class __private(Entity[AccountProps]):
        def __init__(self, props: AccountProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: AccountProps, id: str = None) -> Result[AccountProps]:
        """create account object"""

        guard_result = Guard.against_null_or_empty_bulk(
            **{"username": props.username, "password": props.password}
        )

        if guard_result is not None and not guard_result.succeeded:
            return Result.fail(guard_result.message)

        account = cls.__private(props, id)

        if account.props.password:
            account.props.password = cls.__password_encrypt(account.props.password)

        return Result.ok(account.props)

    @classmethod
    def __password_encrypt(cls, password) -> bytes:
        """Enctrypt password"""

        return PasswordHash.encrypt(password)

    @classmethod
    def compare(cls, hash_pass: str, comparison_pass: bytes) -> bool:
        """Verify if password iblacks valid or not"""

        if hash_pass and comparison_pass:

            return PasswordHash.compare(hash_pass, comparison_pass)

        return Result.fail("Complete the parameters to compare passwords")
