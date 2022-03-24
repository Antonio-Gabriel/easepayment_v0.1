from uuid import uuid4
from dataclasses import dataclass
from .entityprops import ClassRelatedCourseProps

from packages.server._shared.src.core.logic import Result
from packages.server._shared.src.core.domain import Entity


@dataclass
class ClassRelatedCoursePropsResult(ClassRelatedCourseProps):
    id: str = None


class ClassRelatedCourse:
    class __private(Entity[ClassRelatedCourseProps]):
        def __init__(self, props: ClassRelatedCourseProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: ClassRelatedCourseProps, id: str = None):
        """Create a new ClassRelatedCourse"""

        if not id:
            id = uuid4()

        class_related_props = cls.__private(props, id)

        return Result.ok(
            ClassRelatedCoursePropsResult(
                id=id,
                classId=class_related_props.props.classId,
                courseId=class_related_props.props.courseId,
                price=class_related_props.props.price,
            )
        )
