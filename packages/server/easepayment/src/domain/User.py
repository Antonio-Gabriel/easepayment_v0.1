from packages.server._shared.src.core.domain import Entity
from packages.server._shared.src.core.logic import Result

from uuid import uuid4
from dataclasses import dataclass
from .entityprops import UserProps


@dataclass
class UserPropsResult(UserProps):
    id: str = None


class User:
    class __private(Entity[UserProps]):
        def __init__(self, props: UserProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: UserProps, id: int = None):
        """create owner object"""

        if not id:
            id = uuid4()

        if not props.accountId and not props.ownerId:
            return Result.fail("Invalid arguments, please check your arguments!")

        user = cls.__private(props, id)

        return Result.ok(
            UserPropsResult(
                id=id,
                accountId=user.props.accountId,
                ownerId=user.props.ownerId,
            )
        )
