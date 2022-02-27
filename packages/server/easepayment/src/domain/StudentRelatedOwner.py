from packages.server._shared.src.core.domain import Entity

from .entityprops import StudentRelatedOwnerProps


class StudentRelatedOwner:
    class __private(Entity[StudentRelatedOwnerProps]):
        def __init__(self, props: StudentRelatedOwnerProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: StudentRelatedOwnerProps, id: int = None):
        """Create a new ClassRelatedCourse"""

        student_related_owner = cls.__private(props, id)

        return student_related_owner
