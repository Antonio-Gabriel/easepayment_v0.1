from dataclasses import dataclass
from packages.server._shared.src.core.logic import Result, UseCaseError


@dataclass
class IUseCaseErrorError:
    message: str


class CourseAlreadyExists(Result[UseCaseError]):
    def __init__(self, course: str) -> None:
        super().__init__(
            False,
            IUseCaseErrorError(message=f"The course {course} already exist"),
        )
