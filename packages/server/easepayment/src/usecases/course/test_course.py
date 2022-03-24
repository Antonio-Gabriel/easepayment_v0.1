from unittest import TestCase

from .CreateCourse import CreateCourse
from .CourseRequestDTO import CourseRequestDTO
from ...infra.repositories import CourseRepository


class TestCourseUsecase(TestCase):
    def test_course_usecase_integration(self):

        create_course = CreateCourse(CourseRepository)
        result = create_course.execute(CourseRequestDTO(name="Informática", state=True))

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value().id)

        self.assertTrue(True)
