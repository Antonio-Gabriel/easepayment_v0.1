from packages.server._shared.src.core.domain import Entity
from packages.server._shared.src.core.logic import Result, Guard

from uuid import uuid4
from dataclasses import dataclass
from .validators import PasswordHash
from .entityprops import AccountProps


@dataclass
class AccountPropsResult(AccountProps):
    id: str


class Account:
    class __private(Entity[AccountProps]):
        def __init__(self, props: AccountProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: AccountProps, id: str = None) -> Result[AccountProps]:
        """create account object"""

        if not id:
            id = uuid4()

        guard_result = Guard.against_null_or_empty_bulk(
            **{"username": props.username, "password": props.password}
        )

        if guard_result is not None and not guard_result.succeeded:
            return Result.fail(guard_result.message)

        if props.password:
            props.password = cls.__password_encrypt(props.password)

        account = cls.__private(props, id)

        return Result.ok(
            AccountPropsResult(
                id=id, password=account.props.password, username=account.props.username
            )
        )

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
