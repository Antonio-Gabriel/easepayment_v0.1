from typing import Type
from ...domain import StudentRelatedOwner
from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result
from ...infra.repositories import OwnerRelatedStudentEvent
from ...repositories import IOwnerRelatedStudentRepository
from .StudentAlreadyAssociete import StudentAlreadyAssociete
from .RelatedStudentInOwnerRequestDTO import RelatedStudentInOwnerRequestDTO


class RelatedStudentInOwner(IUseCase[RelatedStudentInOwnerRequestDTO, Result[None]]):
    def __init__(self, related_repo: Type[IOwnerRelatedStudentRepository]) -> None:
        self.__related_repo = related_repo

    def execute(self, request: RelatedStudentInOwnerRequestDTO) -> Result[None]:
        """Related Student"""

        student_already_associete = self.__related_repo.find_related_student(
            request.ownerId, request.studentId
        )

        if student_already_associete:
            return StudentAlreadyAssociete(request.studentId)

        related_result = StudentRelatedOwner.create(
            RelatedStudentInOwnerRequestDTO(
                studentId=request.studentId, ownerId=request.ownerId
            )
        )

        if related_result.error_value():
            return Result.fail(related_result.error_value())

        related_event = OwnerRelatedStudentEvent(self.__related_repo)

        related_save_result = related_event.dispatch(
            related_result.get_value().props.ownerId,
            related_result.get_value().props.studentId,
        )

        if related_save_result:
            return Result.ok(related_result.get_value())
