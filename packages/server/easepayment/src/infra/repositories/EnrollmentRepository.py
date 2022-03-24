from sqlalchemy.sql import select
from ..sqlAlchemy import engine, enrollment

from ...repositories import IEnrollmentRepository

from ...domain.entityprops import EnrollmentProps


class EnrollmentRepository(IEnrollmentRepository):
    def save(enrollment_props: EnrollmentProps):
        """Save enrollment"""

        connection = engine.connect()
        statement = enrollment.insert()

        result = connection.execute(
            statement,
            {
                "class_related_course_id": enrollment_props.class_related_course_id,
                "student_id": enrollment_props.student_id,
            },
        )

        return result

    def delete(enrollment_props: EnrollmentProps):
        """delete enrollment"""
