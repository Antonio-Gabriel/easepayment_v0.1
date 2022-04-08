from sqlalchemy.sql import select
from ..sqlAlchemy import engine, student

from ...repositories import IStudentRepository

from ...domain.entityprops import StudentProps


class StudentRepository(IStudentRepository):
    def find_by_email(email: str):
        """Find student by email"""

        connection = engine.connect()
        query = select(student).where(student.c.email == email)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def find_by_phone(phone: str):
        """Find student by phone number"""

        connection = engine.connect()
        query = select(student).where(student.c.phone == phone)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def find_by_process(process: str):
        """Find student by phone number"""

        connection = engine.connect()
        query = select(student).where(student.c.process == process)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def get():
        """Get All students"""
        connection = engine.connect()
        query = select(student)
        result = connection.execute(query)

        row = result.fetchall()

        result.close()

        return row

    def get_by_id(student_id: str):
        """Get student by id"""
        connection = engine.connect()
        query = select(student).where(student.c.id == student_id)
        result = connection.execute(query)

        row = result.fetchone()

        result.close()

        return row

    def save(student_props: StudentProps):
        """Save student into db"""

        connection = engine.connect()
        result = connection.execute(
            student.insert(),
            {
                "id": student_props.id,
                "name": student_props.name,
                "email": student_props.email,
                "phone": student_props.phone,
                "process": student_props.process,
                "district": student_props.district,
                "location": student_props.location,
                "avatar": student_props.avatar,
                "studentId": student_props.studentId,
            },
        )

        return result

    def update(student_props: StudentProps):
        """Update student into db"""

        connection = engine.connect()
        statement = (
            student.update()
            .values(
                {
                    student.c.name: student_props.name,
                    student.c.phone: student_props.phone,
                    student.c.email: student_props.email,
                    student.c.district: student_props.district,
                    student.c.location: student_props.location,
                }
            )
            .where(student.c.process == student_props.process)
        )

        result = connection.execute(statement)

        return result

    def delete(process: str):
        """Delete student into db"""

        connection = engine.connect()
        statement = student.delete().where(student.c.process == process)

        result = connection.execute(statement)

        return result
