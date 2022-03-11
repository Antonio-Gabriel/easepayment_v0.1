from dataclasses import dataclass
from packages.server._shared.src.core.logic import Result, UseCaseError


@dataclass
class IUseCaseErrorError:
    message: str


class ProcessAlreadyExists(Result[UseCaseError]):
    def __init__(self, process: str) -> None:
        super().__init__(
            False,
            IUseCaseErrorError(
                message=f"The process {process} associated for this student already exist"
            ),
        )
