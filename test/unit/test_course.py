from unittest import TestCase

from packages.server.easepayment.src.domain import Course
from packages.server.easepayment.src.domain.entityprops import CourseProps

class TestCourseEntity(TestCase):

    def test_course_entity(self):

        course = Course.create(CourseProps(
            name="AG"            
        ))

        print(course.props.state)

        self.assertTrue(course)