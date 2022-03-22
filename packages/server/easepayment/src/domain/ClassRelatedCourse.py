from packages.server._shared.src.core.domain import Entity
from packages.server._shared.src.core.logic import Result

from .entityprops import ClassRelatedCourseProps


class ClassRelatedCourse:
    class __private(Entity[ClassRelatedCourseProps]):
        def __init__(self, props: ClassRelatedCourseProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: ClassRelatedCourseProps, id: int = None):
        """Create a new ClassRelatedCourse"""

        class_related_props = cls.__private(props, id)

        return Result.ok(class_related_props)
