from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IOwnerRepository
from packages.server._shared.src.core.logic import Result


class GetOwnderById(IUseCase[None, Result[None]]):
    def __init__(self, owner_repo: Type[IOwnerRepository]) -> None:
        self.__owner_repo = owner_repo

    def execute(self, owner_id: str) -> Result[None]:
        """Get owner by id"""

        owner_by_id = self.__owner_repo.get_by_id(owner_id)

        if owner_by_id:

            return Result.ok(owner_by_id)
