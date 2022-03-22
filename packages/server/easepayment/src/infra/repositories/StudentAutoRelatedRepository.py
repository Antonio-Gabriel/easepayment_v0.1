from sqlalchemy.sql import select
from ..sqlAlchemy import engine, student

from ...domain.entityprops import StudentProps
from ...repositories import IStudentAutoRelated


class StudentAutoRelatedRepository(IStudentAutoRelated):
    def save(owner_student_id: str, student_id: str):
        """Related owner with student"""

        connection = engine.connect()

        statement = (
            student.update()
            .where(student.c.id == owner_student_id)
            .values(student_id=student_id)
        )

        result = connection.execute(statement)

        return result

    def find_related_student(owner_student_id: str, student_id: str):
        """Find related student"""

        connection = engine.connect()
        query = select(student).where(
            student.c.id == owner_student_id, student.c.student_id == student_id
        )
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def delete(related_props: StudentProps):
        """delete stutend related owner into db"""
