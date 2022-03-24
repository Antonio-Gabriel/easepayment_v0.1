from typing import Type
from packages.server._shared import IUseCase

from ...domain import ClassRelatedCourse as ClassRelatedCourseDomain
from packages.server._shared.src.core.logic import Result
from ...repositories import IClasseRelatedCourseRepository
from .ClassRelatedCourseRequestDTO import (
    ClassRelatedCourseRequestDTO,
)


class ClassRelatedCourse(IUseCase[ClassRelatedCourseRequestDTO, Result[None]]):
    def __init__(self, related_repo: Type[IClasseRelatedCourseRepository]) -> None:
        self.__related_repo = related_repo

    def execute(self, request: ClassRelatedCourseRequestDTO) -> Result[None]:
        """Related Student"""

        related_result = ClassRelatedCourseDomain.create(
            ClassRelatedCourseRequestDTO(
                classId=request.classId,
                courseId=request.courseId,
                price=request.price,
            )
        )
        if related_result.error_value():
            return Result.fail(related_result.error_value())

        related_save_result = self.__related_repo.save(related_result.get_value())

        if related_save_result:

            return Result.ok(related_result.get_value())
