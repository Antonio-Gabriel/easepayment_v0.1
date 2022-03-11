from unittest import TestCase

from .CreateStudent import CreateStudent
from .StudentRequestDTO import StudentRequestDTO
from ...infra.repositories import StudentRepository


class TestStudendUseCase(TestCase):
    def test_create_student_usecase(self):

        create_student = CreateStudent(StudentRepository)

        result = create_student.execute(
            StudentRequestDTO(
                name="António Gabriel",
                email="antoniocampos@gmail.com",
                phone="923434222",
                process=2000,
                avatar="",
                district="Hoji-ya-henda",
                location="Cazenga",
                studentId="",
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        print(result.get_value().id)

        self.assertTrue(True)
