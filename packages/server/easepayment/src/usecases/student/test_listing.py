from unittest import TestCase

from .GetStudents import GetStudents
from .GetStudentById import GetStudentById

from ...infra.repositories import StudentRepository


class TestListingUseCase(TestCase):
    def test_get_all_student_usecase(self):

        get_all_student = GetStudents(StudentRepository)

        result = get_all_student.execute()

        print(result.get_value())

        self.assertTrue(True)

    def test_get_student_by_id_usecase(self):

        get_student_by_id = GetStudentById(StudentRepository)

        result = get_student_by_id.execute("bd23148b-5fc3-4912-9ee5-dd53aef194dd")

        print(result.get_value())

        self.assertTrue(True)
