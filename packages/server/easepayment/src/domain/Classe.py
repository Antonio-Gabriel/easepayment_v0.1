from uuid import uuid4
from .entityprops import ClassProps

from packages.server._shared.src.core.domain import Entity


class Classe:
    class __private(Entity[ClassProps]):
        def __init__(self, props: ClassProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: ClassProps, id: int = None):
        """create class object"""

        if not id:
            id = uuid4()

        classe = cls.__private(props, id)

        return classe
