from unittest import TestCase

from .ClassRelatedCourse import ClassRelatedCourse
from ...infra.repositories import ClasseRelatedCourseRepository
from .ClassRelatedCourseRequestDTO import ClassRelatedCourseRequestDTO

from .DeleteClassRelatedCourse import DeleteClassRelatedCourse


class TestClassRelatedCourseUsecase(TestCase):
    def test_class_related_course_usecase_integration(self):

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

    def test_delete_related_class_course(self):

        delete_class_related_course = DeleteClassRelatedCourse(
            ClasseRelatedCourseRepository
        )
        result = delete_class_related_course.execute(
            id="8590a89e-bb7d-43fe-b068-471b15c37748"
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)
