from typing import Type
from .UserRequestDTO import UserRequestDTO
from ...repositories import IUserRepository

from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result


class DeleteUser(IUseCase[UserRequestDTO, Result[None]]):
    def __init__(self, user_repo: Type[IUserRepository]) -> None:
        self.__user_repo = user_repo

    def execute(self, user_id: str) -> Result[None]:

        user_removed_result = self.__user_repo.remove(user_id)

        if user_removed_result:
            return Result.ok("User Removed")
