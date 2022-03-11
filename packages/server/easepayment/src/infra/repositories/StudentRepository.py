from ...repositories import IStudentRepository

from ...domain.entityprops import StudentProps

from sqlalchemy.sql import select
from ..sqlAlchemy import engine, student


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
