from dataclasses import dataclass
from packages.server._shared.src.core.logic import Result, UseCaseError


@dataclass
class IUseCaseErrorError:
    message: str


class PhoneAlreadyExists(Result[UseCaseError]):
    def __init__(self, phone: str) -> None:
        super().__init__(
            False,
            IUseCaseErrorError(
                message=f"The phone {phone} associated for this contact already exist"
            ),
        )
