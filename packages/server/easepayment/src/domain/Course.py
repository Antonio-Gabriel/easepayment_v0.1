from datetime import datetime

from .entityprops import CourseProps

from packages.server._shared.src.core.domain import Entity


class Course:
    class __private(Entity[CourseProps]):
        def __init__(self, props: CourseProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: CourseProps, id: str = None):
        """create course object"""

        course = cls.__private(
            CourseProps(
                name=props.name,
                state=props.state,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            id,
        )

        return course
