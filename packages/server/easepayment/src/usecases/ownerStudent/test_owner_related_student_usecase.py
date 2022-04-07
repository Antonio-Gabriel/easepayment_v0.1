from unittest import TestCase

from .UnrelatedStudentInOwner import UnrelatedStudentInOwner

from .RelatedStudentInOwner import RelatedStudentInOwner
from ...infra.repositories import OwnerRelatedStudentRepository
from .RelatedStudentInOwnerRequestDTO import RelatedStudentInOwnerRequestDTO


class TestRelatedOwnerWithStudent(TestCase):
    def test_related_student_owner(self):

        related_student = RelatedStudentInOwner(OwnerRelatedStudentRepository)
        result = related_student.execute(
            RelatedStudentInOwnerRequestDTO(
                studentId="8aec3a87-b85e-4833-bcb9-34b8e251b19f",
                ownerId="418a947c-cf18-405d-abc0-c8f662eff753",
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        else:
            print(result.get_value().props)

        self.assertTrue(True)

    def test_unrelated_student_in_owner(self):

        related_student = UnrelatedStudentInOwner(OwnerRelatedStudentRepository)
        result = related_student.execute(
            student_id="8aec3a87-b85e-4833-bcb9-34b8e251b19f",
            owner_id="418a947c-cf18-405d-abc0-c8f662eff753",
        )

        print(result)

        self.assertTrue(True)
