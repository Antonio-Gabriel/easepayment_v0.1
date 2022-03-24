from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IOwnerRepository
from packages.server._shared.src.core.logic import Result


class GetOwners(IUseCase[None, Result[None]]):
    def __init__(self, owner_repo: Type[IOwnerRepository]) -> None:
        self.__owner_repo = owner_repo

    def execute(self) -> Result[None]:
        """Get all owners"""

        all_owners = self.__owner_repo.get()

        if all_owners:

            return Result.ok(all_owners)
