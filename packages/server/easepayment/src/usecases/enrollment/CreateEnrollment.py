from typing import Type
from ...domain import Enrollment
from packages.server._shared import IUseCase
from ...repositories import IEnrollmentRepository

from .EnrollmentRequestDTO import EnrollmentRequestDTO
from packages.server._shared.src.core.logic import Result


class CreateEnrollment(IUseCase[EnrollmentRequestDTO, Result[None]]):
    def __init__(self, enrollment_repo: Type[IEnrollmentRepository]) -> None:
        self.__enrollment_repo = enrollment_repo

    def execute(self, request: EnrollmentRequestDTO) -> Result[None]:
        """Create enrollement"""

        enrollment_result = Enrollment.create(
            EnrollmentRequestDTO(
                class_related_course_id=request.class_related_course_id,
                student_id=request.student_id,
            )
        )

        if enrollment_result.error_value():
            return Result.fail(enrollment_result.error_value())

        enrollment_save_result = self.__enrollment_repo.save(
            enrollment_result.get_value()
        )

        if enrollment_save_result:

            return Result.ok(enrollment_result.get_value())
