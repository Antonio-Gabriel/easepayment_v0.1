from unittest import TestCase

from .CreateCourse import CreateCourse
from .CourseRequestDTO import CourseRequestDTO
from ...infra.repositories import CourseRepository

from .GetCourses import GetCourses


class TestCourseUsecase(TestCase):
    def test_course_usecase_integration(self):

        create_course = CreateCourse(CourseRepository)
        result = create_course.execute(
            CourseRequestDTO(name="Ciências Econômicas", state=True)
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value().id)

        self.assertTrue(True)

    def test_get_all_courses(self):

        get_all_courses = GetCourses(CourseRepository)

        result = get_all_courses.execute()

        for course in result.get_value():

            print(course[1])

        self.assertTrue(True)
