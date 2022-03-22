from uuid import uuid4
from dataclasses import dataclass
from .entityprops import UserProps

from packages.server._shared.src.core.logic import Result
from packages.server._shared.src.core.domain import Entity


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

        if not props.account_id and not props.owner_id and not props.student_id:
            return Result.fail("Invalid arguments, please check your arguments!")

        user = cls.__private(props, id)

        return Result.ok(
            UserPropsResult(
                id=id,
                student_id=user.props.student_id,
                account_id=user.props.account_id,
                owner_id=user.props.owner_id,
            )
        )
