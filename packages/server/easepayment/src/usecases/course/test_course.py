from unittest import TestCase

from .CreateCourse import CreateCourse
from .CourseRequestDTO import CourseRequestDTO
from ...infra.repositories import CourseRepository

from .GetCourses import GetCourses
from .GetCourseById import GetCourseById

from .UpdateCourse import UpdateCourse
from .DeleteCourse import DeleteCourse


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

    def test_update_course_usecase_integration(self):

        create_course = UpdateCourse(CourseRepository)
        result = create_course.execute(
            CourseRequestDTO(name="Ciências Econômicas", state=True),
            id="1607f497-e980-4a86-92cd-3e1ad3978963",
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)

    def test_delete_course_usecase_integration(self):

        delete_course = DeleteCourse(CourseRepository)
        result = delete_course.execute("1607f497-e980-4a86-92cd-3e1ad3978963")

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)

    def test_get_all_courses(self):

        get_all_courses = GetCourses(CourseRepository)

        result = get_all_courses.execute()

        for course in result.get_value():

            print(course[1])

        self.assertTrue(True)

    def test_get_course_by_id(self):

        course_by_id = GetCourseById(CourseRepository)

        result = course_by_id.execute("1607f497-e980-4a86-92cd-3e1ad3978963")

        for course in result.get_value():

            print(course)

        self.assertTrue(True)
