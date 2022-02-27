from packages.server._shared.src.core.domain import Entity

from .entityprops import UserProps


class User:
    class __private(Entity[UserProps]):
        def __init__(self, props: UserProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: UserProps, id: int = None):
        """create owner object"""

        user = cls.__private(props, id)

        return user
