from typing import Type
from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result
from ...repositories import IOwnerRelatedStudentRepository


class GetStudentsRelatedOwner(IUseCase[None, Result[None]]):
    def __init__(self, related_repo: Type[IOwnerRelatedStudentRepository]) -> None:
        self.__related_repo = related_repo

    def execute(self, ownerId: str) -> Result[None]:
        """Get students related owner"""

        students = self.__related_repo.get(ownerId)

        if students:
            return Result.ok(students)
