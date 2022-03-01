from dataclasses import dataclass
from packages.server._shared.src.core.logic import Result, UseCaseError


@dataclass
class IUseCaseErrorError:
    message: str


class OwnerAlreadyExists(Result[UseCaseError]):
    def __init__(self, email: str) -> None:
        super().__init__(
            False,
            IUseCaseErrorError(
                message=f"The email {email} associated for this contact already exist"
            ),
        )
