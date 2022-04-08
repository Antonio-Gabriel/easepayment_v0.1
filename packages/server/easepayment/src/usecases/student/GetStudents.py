from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IStudentRepository
from packages.server._shared.src.core.logic import Result


class GetStudents(IUseCase[None, Result[None]]):
    def __init__(self, student_repo: Type[IStudentRepository]) -> None:
        self.__student_repo = student_repo

    def execute(self) -> Result[None]:
        """Get all students"""

        all_students = self.__student_repo.get()

        if all_students:

            return Result.ok(all_students)
