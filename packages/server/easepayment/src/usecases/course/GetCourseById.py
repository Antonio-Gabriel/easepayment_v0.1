from typing import Type
from packages.server._shared import IUseCase
from ...repositories import ICourseRepository
from packages.server._shared.src.core.logic import Result


class GetCourseById(IUseCase[None, Result[None]]):
    def __init__(self, course_repo: Type[ICourseRepository]) -> None:
        self.__course_repo = course_repo

    def execute(self, course_id: str) -> Result[None]:
        """Get course by id"""

        course_by_id = self.__course_repo.get_by_id(course_id)

        if course_by_id:

            return Result.ok(course_by_id)
