from typing import Type
from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result
from ...repositories import IOwnerRelatedStudentRepository


class UnrelatedStudentInOwner(IUseCase[None, Result[None]]):
    def __init__(self, related_repo: Type[IOwnerRelatedStudentRepository]) -> None:
        self.__related_repo = related_repo

    def execute(self, owner_id: str, student_id: str) -> Result[None]:
        """Unrelated Student"""

        unrelated_owner_in_student = self.__related_repo.delete(
            student_id=student_id, owner_id=owner_id
        )

        if unrelated_owner_in_student:
            return Result.ok("Unrelated student in owner")
