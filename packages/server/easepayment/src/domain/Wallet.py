from .entityprops import WallerProps

from packages.server._shared.src.core.domain import Entity


class Wallet:
    class __private(Entity[WallerProps]):
        def __init__(self, props: WallerProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: WallerProps, id: int = None):
        """create owner object"""

        wallet = cls.__private(props, id)

        return wallet
