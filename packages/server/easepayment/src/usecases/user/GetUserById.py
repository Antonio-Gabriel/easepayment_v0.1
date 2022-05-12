from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IUserRepository
from packages.server._shared.src.core.logic import Result


class GetUserById(IUseCase[None, Result[None]]):
    def __init__(self, user_repo: Type[IUserRepository]) -> None:
        self.__user_repo = user_repo

    def execute(self, user_id: str) -> Result[None]:
        """Get user by id"""

        get_user_by_id = self.__user_repo.get(user_id)

        if get_user_by_id:

            return Result.ok(get_user_by_id)
