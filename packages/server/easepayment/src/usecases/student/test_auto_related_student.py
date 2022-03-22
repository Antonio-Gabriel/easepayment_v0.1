from unittest import TestCase

from .AutoRelatedStudent import AutoRelatedStudent
from .AutoRelatedStudentDTO import AutoRelatedStudentDTO
from ...infra.repositories import StudentAutoRelatedRepository


class TestAutoRelatedStudent(TestCase):
    def test_auto_related_student(self):

        auto_related = AutoRelatedStudent(StudentAutoRelatedRepository)

        result = auto_related.execute(
            AutoRelatedStudentDTO(
                owner_studentId="dfbe6494-a57c-49a8-82a5-ecbb94247e19",
                studentId="aaec692c-7d68-43a2-8745-e560b7b5215b",
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value().student_id)

        self.assertTrue(True)
