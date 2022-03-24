from typing import Type
from packages.server._shared import IUseCase
from ...repositories import ICourseRepository
from packages.server._shared.src.core.logic import Result


class DeleteCourse(IUseCase[None, Result[None]]):
    def __init__(self, course_repo: Type[ICourseRepository]) -> None:
        self.__course_repo = course_repo

    def execute(self, id: str) -> Result[None]:
        """Delete course"""

        course_deleted_result = self.__course_repo.delete(id)

        if course_deleted_result:

            return Result.ok("Deleted course")
