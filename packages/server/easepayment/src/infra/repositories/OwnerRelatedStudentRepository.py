from sqlalchemy.sql import select
from ..sqlAlchemy import engine, owner_related_student

from ...domain.entityprops import StudentRelatedOwnerProps
from ...repositories import IOwnerRelatedStudentRepository


class OwnerRelatedStudentRepository(IOwnerRelatedStudentRepository):
    def save(related_props: StudentRelatedOwnerProps):
        """Related owner with student"""
        connection = engine.connect()
        result = connection.execute(
            owner_related_student.insert(),
            {
                "owner_id": related_props.ownerId,
                "student_id": related_props.studentId,
            },
        )

        return result

    def find_related_student(owner_id: str, student_id: str):
        """Find related student"""
        connection = engine.connect()
        query = select(owner_related_student).where(
            owner_related_student.c.owner_id == owner_id,
            owner_related_student.c.student_id == student_id,
        )
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def delete(student_id: str, owner_id: str):
        """delete stutend related owner into db"""
        connection = engine.connect()
        statement = owner_related_student.delete().where(
            owner_related_student.c.owner_id == owner_id,
            owner_related_student.c.student_id == student_id,
        )

        result = connection.execute(statement)

        return result
