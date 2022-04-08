from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IStudentAutoRelated

from .AutoRelatedStudentDTO import AutoRelatedStudentDTO
from packages.server._shared.src.core.logic import Result


class UnrelatedStudent(IUseCase[AutoRelatedStudentDTO, Result[None]]):
    def __init__(self, student_repo: Type[IStudentAutoRelated]) -> None:
        self.__student_repo = student_repo

    def execute(self, request: AutoRelatedStudentDTO) -> Result[None]:
        """Unrelated relation of student"""

        student_already_associeted = self.__student_repo.find_related_student(
            request.owner_studentId, request.studentId
        )

        if not student_already_associeted:
            return Result.fail("Student don't exists!.")

        student_result = AutoRelatedStudentDTO(
            studentId=request.studentId, owner_studentId=request.owner_studentId
        )

        unrelated_result = self.__student_repo.unrelated(
            owner_student_id=request.owner_studentId, student_id=request.studentId
        )

        if unrelated_result:

            return Result.ok(student_result)
