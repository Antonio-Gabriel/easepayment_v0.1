from uuid import uuid4
from dataclasses import dataclass
from .entityprops import OwnerProps
from .validators import Email, Phone

from packages.server._shared.src.core.domain import Entity
from packages.server._shared.src.core.logic import Result, Guard


@dataclass
class OwnerPropsResult(OwnerProps):
    id: str


class Owner:
    class __private(Entity[OwnerProps]):
        def __init__(self, props: OwnerProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: OwnerProps, id: int = None):
        """create owner object"""

        if not id:
            id = uuid4()

        guard_result = Guard.against_null_or_empty_bulk(
            **{"name": props.name, "email": props.email, "phone": props.phone}
        )

        if guard_result is not None and not guard_result.succeeded:
            return Result.fail(guard_result.message)

        if not Email.is_valid(props.email):
            return Result.fail("Invalid email address, pleace check your email!")

        if not Phone.is_valid(props.phone):
            return Result.fail("Invalid phone number, pleace check your phone number!")

        owner = cls.__private(props, id)

        return Result.ok(
            OwnerPropsResult(
                id=id,
                name=owner.props.name,
                email=owner.props.email,
                phone=owner.props.phone,
            )
        )
