from unittest import TestCase

from .CreateStudent import CreateStudent
from .UpdateStudent import UpdateStudent
from .DeleteStudent import DeleteStudent

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

    def test_update_student_usecase(self):

        update_student = UpdateStudent(StudentRepository)

        result = update_student.execute(
            StudentRequestDTO(
                name="Kiala Danile Gabriel",
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

    def test_delete_student_usecase(self):

        delete_student = DeleteStudent(StudentRepository)

        result = delete_student.execute(process=2100)

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)
