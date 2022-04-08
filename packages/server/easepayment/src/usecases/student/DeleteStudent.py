from typing import Type
from packages.server._shared import IUseCase

from ...repositories import IStudentRepository
from packages.server._shared.src.core.logic import Result


class DeleteStudent(IUseCase[None, Result[None]]):
    def __init__(self, student_repo: Type[IStudentRepository]) -> None:
        self.__student_repo = student_repo

    def execute(self, process: str) -> Result[None]:
        """Delete owner"""

        get_current_student = self.__student_repo.find_by_process(process)

        if not get_current_student:
            return Result.fail("Student Not exists")

        student_save_result = self.__student_repo.delete(process)

        if student_save_result:

            return Result.ok("Student is deleted")
