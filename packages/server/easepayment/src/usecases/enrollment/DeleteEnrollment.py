from typing import Type
from ...domain import Enrollment
from packages.server._shared import IUseCase
from ...domain.entityprops import EnrollmentProps
from ...repositories import IEnrollmentRepository


from packages.server._shared.src.core.logic import Result


class DeleteEnrollment(IUseCase[None, Result[None]]):
    def __init__(self, enrollment_repo: Type[IEnrollmentRepository]) -> None:
        self.__enrollment_repo = enrollment_repo

    def execute(self, class_related_course_id: str, student_id: str) -> Result[None]:
        """Create enrollement"""

        enrollment_save_result = self.__enrollment_repo.delete(
            class_related_course_id, student_id
        )

        if enrollment_save_result:

            return Result.ok("Enrollment deleted")
