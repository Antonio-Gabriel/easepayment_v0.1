from packages.server._shared.src.core.domain import Entity

from .entityprops import OwnerProps


class Owner:
    class __private(Entity[OwnerProps]):
        def __init__(self, props: OwnerProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: OwnerProps, id: int = None):
        """create owner object"""

        owner = cls.__private(props, id)

        return owner
