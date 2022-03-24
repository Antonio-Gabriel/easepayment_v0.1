from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass

from .entityprops import CourseProps

from packages.server._shared.src.core.logic import Result
from packages.server._shared.src.core.domain import Entity


@dataclass
class CoursePropsResult(CourseProps):
    id: str = None


class Course:
    class __private(Entity[CourseProps]):
        def __init__(self, props: CourseProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: CourseProps, id: str = None):
        """create course object"""

        if not id:
            id = uuid4()

        course = cls.__private(
            CourseProps(
                name=props.name,
                state=props.state,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            id,
        )

        return Result.ok(
            CoursePropsResult(
                id=id,
                name=course.props.name,
                state=course.props.state,
                created_at=course.props.created_at,
                updated_at=course.props.updated_at,
            )
        )
