from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass

from .entityprops import EnrollmentProps

from packages.server._shared.src.core.logic import Result
from packages.server._shared.src.core.domain import Entity


@dataclass
class EnrollmentResult(EnrollmentProps):
    id: str = None


class Enrollment:
    class __private(Entity[EnrollmentProps]):
        def __init__(self, props: EnrollmentProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: EnrollmentProps, id: str = None):
        """create enrollment object"""

        if not id:
            id = uuid4()

        enrollment = cls.__private(
            EnrollmentResult(
                class_related_course_id=props.class_related_course_id,
                student_id=props.student_id,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            id,
        )

        return Result.ok(
            EnrollmentResult(
                id=id,
                class_related_course_id=enrollment.props.class_related_course_id,
                student_id=enrollment.props.student_id,
                created_at=enrollment.props.created_at,
                updated_at=enrollment.props.updated_at,
            )
        )
