from dataclasses import dataclass
from packages.server._shared.src.core.logic import Result, UseCaseError


@dataclass
class IUseCaseErrorError:
    message: str


class MonthAlreadyPayed(Result[UseCaseError]):
    def __init__(self, month: str) -> None:
        super().__init__(
            False,
            IUseCaseErrorError(message=f"The month {month} is already payed"),
        )
