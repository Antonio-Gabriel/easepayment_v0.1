from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass
from .entityprops import WallerProps

from packages.server._shared.src.core.logic import Result
from packages.server._shared.src.core.domain import Entity


@dataclass
class WallerPropsResult(WallerProps):
    id: str = None


class Wallet:
    class __private(Entity[WallerProps]):
        def __init__(self, props: WallerProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: WallerProps, id: int = None):
        """create wallet object"""

        if not id:
            id = uuid4()

        wallet = cls.__private(props, id)

        return Result.ok(
            WallerPropsResult(
                id=id,
                balance=wallet.props.balance,
                userId=wallet.props.userId,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
        )
