from unittest import TestCase

from .ClassRelatedCourse import ClassRelatedCourse
from ...infra.repositories import ClasseRelatedCourseRepository
from .ClassRelatedCourseRequestDTO import ClassRelatedCourseRequestDTO


class TestClassRelatedCourseUsecase(TestCase):
    def test_owner_usecase_integration(self):

        create_class_related_course = ClassRelatedCourse(ClasseRelatedCourseRepository)
        result = create_class_related_course.execute(
            ClassRelatedCourseRequestDTO(
                classId="1ffb034e-5f47-43f7-b328-48d4eece78bc",
                courseId="1d4ddda2-9077-4c42-93af-6c5570579812",
                price=12000.00,
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value().id)

        self.assertTrue(True)
