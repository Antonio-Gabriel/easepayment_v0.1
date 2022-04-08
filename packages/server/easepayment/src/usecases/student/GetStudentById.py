from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IStudentRepository
from packages.server._shared.src.core.logic import Result


class GetStudentById(IUseCase[None, Result[None]]):
    def __init__(self, student_repo: Type[IStudentRepository]) -> None:
        self.__student_repo = student_repo

    def execute(self, student_id: str) -> Result[None]:
        """Get student by id"""

        student_by_id = self.__student_repo.get_by_id(student_id)

        if student_by_id:

            return Result.ok(student_by_id)
