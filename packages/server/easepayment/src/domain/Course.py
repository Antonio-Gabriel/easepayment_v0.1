from packages.server._shared.src.core.domain import Entity

from .entityprops import CourseProps


class Course:
    class __private(Entity[CourseProps]):
        def __init__(self, props: CourseProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: CourseProps, id: str = None):
        """create course object"""

        course = cls.__private(props, id)

        return course
