from sqlalchemy.sql import select
from ..sqlAlchemy import (
    engine,
    owner_related_student,
    student,
    owner,
    enrollment,
    classe_related_course,
    classe,
    course,
)

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

    def get(ownerId: str):
        """Get"""
        connection = engine.connect()
        query = (
            select(
                [
                    student.c.id,
                    student.c.process,
                    student.c.name,
                    student.c.email,
                    student.c.phone,
                    classe.c.name,
                    course.c.name,
                ]
            )
            .select_from(
                owner_related_student.outerjoin(
                    student, owner_related_student.c.student_id == student.c.id
                ).outerjoin(owner, owner_related_student.c.owner_id == owner.c.id)
            )
            .select_from(
                enrollment.outerjoin(
                    classe_related_course,
                    enrollment.c.class_related_course_id == classe_related_course.c.id,
                )
                .outerjoin(classe, classe.c.id == classe_related_course.c.classe_id)
                .outerjoin(course, course.c.id == classe_related_course.c.course_id)
            )
            .where(owner.c.id == ownerId)
        )

        result = connection.execute(query).fetchall()

        return result

    def delete(student_id: str, owner_id: str):
        """delete stutend related owner into db"""
        connection = engine.connect()
        statement = owner_related_student.delete().where(
            owner_related_student.c.owner_id == owner_id,
            owner_related_student.c.student_id == student_id,
        )

        result = connection.execute(statement)

        return result
