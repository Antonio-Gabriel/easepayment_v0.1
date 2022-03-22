from dataclasses import dataclass
from packages.server._shared.src.core.logic import Result, UseCaseError


@dataclass
class IUseCaseErrorError:
    message: str


class StudentAlreadyRegister(Result[UseCaseError]):
    def __init__(self, student: str) -> None:
        super().__init__(
            False,
            IUseCaseErrorError(
                message=f"The student {student} already associente for this owner"
            ),
        )
