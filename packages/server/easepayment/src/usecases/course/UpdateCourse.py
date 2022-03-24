from re import S
from typing import Type
from ...domain import Course
from packages.server._shared import IUseCase
from .CourseRequestDTO import CourseRequestDTO
from ...repositories import ICourseRepository
from .CourseAlreadyExists import CourseAlreadyExists
from packages.server._shared.src.core.logic import Result


class UpdateCourse(IUseCase[CourseRequestDTO, Result[None]]):
    def __init__(self, course_repo: Type[ICourseRepository]) -> None:
        self.__course_repo = course_repo

    def execute(self, request: CourseRequestDTO, id: str) -> Result[None]:
        """Update course"""

        get_course_by_id = self.__course_repo.get_by_id(id)

        course_result = Course.create(
            CourseRequestDTO(name=request.name, state=request.state), id
        )

        if course_result.error_value():
            return Result.fail(course_result.error_value())

        if get_course_by_id[1] == request.name:

            course_update_result = self.__course_repo.update(course_result.get_value())

            if course_update_result:

                return Result.ok(course_result.get_value())

        course_already_exists = self.__course_repo.find_course(request.name)

        if course_already_exists:
            return CourseAlreadyExists(request.name)

        course_update_result = self.__course_repo.update(course_result.get_value())

        if course_update_result:

            return Result.ok(course_result.get_value())
