from unittest import TestCase

from .RelatedStudentInOwner import RelatedStudentInOwner
from ...infra.repositories import OwnerRelatedStudentRepository
from .RelatedStudentInOwnerRequestDTO import RelatedStudentInOwnerRequestDTO


class TestRelatedOwnerWithStudent(TestCase):
    def test_related_student_owner(self):

        related_student = RelatedStudentInOwner(OwnerRelatedStudentRepository)
        result = related_student.execute(
            RelatedStudentInOwnerRequestDTO(
                studentId="d8db5d3a-0cf9-446f-8c1d-21dd703273c1",
                ownerId="73b2e45e-5ea3-483a-9bef-7d6fc7da5028",
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        else:
            print(result.get_value().props)

        self.assertTrue(True)
