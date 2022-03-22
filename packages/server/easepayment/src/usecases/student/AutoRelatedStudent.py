from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IStudentAutoRelated

from .AutoRelatedStudentDTO import AutoRelatedStudentDTO
from packages.server._shared.src.core.logic import Result
from ...infra.repositories import StudentAutoRelatedEvent
from .StudentAlreadyAssocieted import StudentAlreadyAssocieted


class AutoRelatedStudent(IUseCase[AutoRelatedStudentDTO, Result[None]]):
    def __init__(self, student_repo: Type[IStudentAutoRelated]) -> None:
        self.__student_repo = student_repo

    def execute(self, request: AutoRelatedStudentDTO) -> Result[None]:
        """Create auto relation of student"""

        student_already_associeted = self.__student_repo.find_related_student(
            request.owner_studentId, request.studentId
        )

        if student_already_associeted:
            return StudentAlreadyAssocieted(request.studentId)

        student_result = AutoRelatedStudentDTO(
            studentId=request.studentId, owner_studentId=request.owner_studentId
        )

        related_event = StudentAutoRelatedEvent(self.__student_repo)

        related_save_result = related_event.dispatch(
            owner_student_id=student_result.owner_studentId,
            student_id=student_result.studentId,
        )

        if related_save_result:

            return Result.ok(student_result)
