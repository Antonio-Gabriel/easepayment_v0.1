from ...domain.entityprops import ClassRelatedCourseProps
from ...repositories import IClasseRelatedCourseRepository

from sqlalchemy.sql import select
from ..sqlAlchemy import engine, classe_related_course


class ClasseRelatedCourseRepository(IClasseRelatedCourseRepository):
    def save(related_props: ClassRelatedCourseProps):
        """Related class with student"""
        connection = engine.connect()
        result = connection.execute(
            classe_related_course.insert(),
            {
                "owner_id": related_props.ownerId,
                "student_id": related_props.studentId,
            },
        )

        return result

    def find_student_associeted(student_id: str):
        """Find related student"""
        connection = engine.connect()
        query = select(classe_related_course).where(
            classe_related_course.c.student_id == student_id,
        )
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def delete(related_props: ClassRelatedCourseProps):
        """delete stutend related owner into db"""
