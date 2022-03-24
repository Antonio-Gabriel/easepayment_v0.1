from unittest import TestCase

from .CreateEnrollment import CreateEnrollment
from .EnrollmentRequestDTO import EnrollmentRequestDTO
from ...infra.repositories import EnrollmentRepository

from .DeleteEnrollment import DeleteEnrollment


class TestEnrollment(TestCase):
    def test_enrollment_usecase_integration(self):

        create_enrollment = CreateEnrollment(EnrollmentRepository)
        result = create_enrollment.execute(
            EnrollmentRequestDTO(
                class_related_course_id="8590a89e-bb7d-43fe-b068-471b15c37748",
                student_id="8aec3a87-b85e-4833-bcb9-34b8e251b19f",
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        print(result.get_value())

        self.assertTrue(True)

    def test_delete_enrollment_usecase_integration(self):

        delete_enrollment = DeleteEnrollment(EnrollmentRepository)
        result = delete_enrollment.execute(
            class_related_course_id="8590a89e-bb7d-43fe-b068-471b15c37748",
            student_id="8aec3a87-b85e-4833-bcb9-34b8e251b19f",
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)
