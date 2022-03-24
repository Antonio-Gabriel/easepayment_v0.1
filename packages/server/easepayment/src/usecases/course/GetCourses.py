from typing import Type
from packages.server._shared import IUseCase
from ...repositories import ICourseRepository
from packages.server._shared.src.core.logic import Result


class GetCourses(IUseCase[None, Result[None]]):
    def __init__(self, course_repo: Type[ICourseRepository]) -> None:
        self.__course_repo = course_repo

    def execute(self) -> Result[None]:
        """Get all course"""

        all_courses = self.__course_repo.get()

        if all_courses:

            return Result.ok(all_courses)
