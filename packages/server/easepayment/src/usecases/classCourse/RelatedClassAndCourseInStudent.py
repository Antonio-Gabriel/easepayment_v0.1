from typing import Type
from packages.server._shared import IUseCase

from ...domain import ClassRelatedCourse
from packages.server._shared.src.core.logic import Result
from ...repositories import IClasseRelatedCourseRepository
from .StudentAlreadyRegister import StudentAlreadyRegister
from .RelatedClassAndCourseInStudentRequestDTO import (
    RelatedClassAndCourseInStudentRequestDTO,
)


class RelatedClassAndCourseInStudent(
    IUseCase[RelatedClassAndCourseInStudentRequestDTO, Result[None]]
):
    def __init__(self, related_repo: Type[IClasseRelatedCourseRepository]) -> None:
        self.__related_repo = related_repo

    def execute(
        self, request: RelatedClassAndCourseInStudentRequestDTO
    ) -> Result[None]:
        """Related Student"""

        student_already_associeted = self.__related_repo.find_student_associeted(
            request.studentId
        )

        if student_already_associeted:
            return StudentAlreadyRegister(request.studentId)

        related_result = ClassRelatedCourse.create(
            RelatedClassAndCourseInStudentRequestDTO(
                classId=request.classId,
                courseId=request.courseId,
                studentId=request.studentId,
                price=request.price,
            )
        )

        if related_result.error_value():
            return Result.fail(related_result.error_value())

        related_save_result = self.__related_repo.save(related_result.get_value())

        if related_save_result:
            return Result.ok(related_result.get_value())
