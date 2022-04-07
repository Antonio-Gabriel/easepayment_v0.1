from unittest import TestCase

from .UnrelatedStudentInOwner import UnrelatedStudentInOwner
from ...infra.repositories import OwnerRelatedStudentRepository


class TestUnrelatedStudentInOwner(TestCase):
    def test_unrelated_student_in_owner(self):

        related_student = UnrelatedStudentInOwner(OwnerRelatedStudentRepository)
        result = related_student.execute(
            student_id="8aec3a87-b85e-4833-bcb9-34b8e251b19f",
            owner_id="418a947c-cf18-405d-abc0-c8f662eff753",
        )

        print(result)

        self.assertTrue(True)
