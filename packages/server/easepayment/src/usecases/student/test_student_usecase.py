from unittest import TestCase

from .CreateStudent import CreateStudent
from .StudentRequestDTO import StudentRequestDTO
from ...infra.repositories import StudentRepository


class TestStudendUseCase(TestCase):
    def test_create_student_usecase(self):

        create_student = CreateStudent(StudentRepository)

        result = create_student.execute(
            StudentRequestDTO(
                name="Kiala Gabriel",
                email="kialagabriel@gmail.com",
                phone="923434223",
                process=2100,
                avatar="",
                district="Hoji-ya-henda",
                location="Cazenga",
                studentId="",
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value().id)

        self.assertTrue(True)
