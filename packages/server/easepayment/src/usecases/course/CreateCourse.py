from re import S
from typing import Type
from ...domain import Course
from packages.server._shared import IUseCase
from .CourseRequestDTO import CourseRequestDTO
from ...repositories import ICourseRepository
from .CourseAlreadyExists import CourseAlreadyExists
from packages.server._shared.src.core.logic import Result


class CreateCourse(IUseCase[CourseRequestDTO, Result[None]]):
    def __init__(self, course_repo: Type[ICourseRepository]) -> None:
        self.__course_repo = course_repo

    def execute(self, request: CourseRequestDTO) -> Result[None]:
        """Create course"""

        course_already_exists = self.__course_repo.find_course(request.name)

        if course_already_exists:
            return CourseAlreadyExists(request.name)

        course_result = Course.create(
            CourseRequestDTO(name=request.name, state=request.state)
        )

        if course_result.error_value():
            return Result.fail(course_result.error_value())

        course_save_result = self.__course_repo.save(course_result.get_value())

        if course_save_result:

            return Result.ok(course_result.get_value())
