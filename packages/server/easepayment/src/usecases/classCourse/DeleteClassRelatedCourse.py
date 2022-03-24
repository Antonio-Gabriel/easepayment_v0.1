from typing import Type
from packages.server._shared import IUseCase

from packages.server._shared.src.core.logic import Result
from ...repositories import IClasseRelatedCourseRepository


class DeleteClassRelatedCourse(IUseCase[any, Result[None]]):
    def __init__(self, related_repo: Type[IClasseRelatedCourseRepository]) -> None:
        self.__related_repo = related_repo

    def execute(self, id: str) -> Result[None]:
        """Related course"""

        related_save_result = self.__related_repo.delete(id)

        if related_save_result:

            return Result.ok("Delete class related course")
