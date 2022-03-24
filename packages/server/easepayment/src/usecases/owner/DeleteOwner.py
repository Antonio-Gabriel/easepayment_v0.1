from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IOwnerRepository
from packages.server._shared.src.core.logic import Result


class DeleteOwner(IUseCase[None, Result[None]]):
    def __init__(self, owner_repo: Type[IOwnerRepository]) -> None:
        self.__owner_repo = owner_repo

    def execute(self, id: str) -> Result[None]:
        """Delete owner"""

        owner_deleted_result = self.__owner_repo.delete(id)

        if owner_deleted_result:

            return Result.ok("Deleted owner")
