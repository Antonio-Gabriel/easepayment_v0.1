from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IClasseRelatedCourseRepository
from packages.server._shared.src.core.logic import Result


class GetClassWithCourse(IUseCase[None, Result[None]]):
    def __init__(self, related_repo: Type[IClasseRelatedCourseRepository]) -> None:
        self.__related_repo = related_repo

    def execute(self) -> Result[None]:
        """Get all class"""

        get_class_with_courses = self.__related_repo.get_class_with_courses()

        if get_class_with_courses:

            return Result.ok(get_class_with_courses)
