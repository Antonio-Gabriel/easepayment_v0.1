from packages.server._shared.src.core.domain import Entity

from .entityprops import StudentProps


class Student:
    class __private(Entity[StudentProps]):
        def __init__(self, props: StudentProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: StudentProps, id: int = None):
        """create owner object"""

        student = cls.__private(props, id)

        return student
