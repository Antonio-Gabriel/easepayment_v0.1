from typing import Type

from packages.server._shared import IUseCase
from ...repositories import IAccountRepository
from packages.server._shared.src.core.logic import Result


class GetAccountById(IUseCase[any, Result[None]]):
    def __init__(self, account_repo: Type[IAccountRepository]) -> None:
        self.__account_repo = account_repo

    def execute(self, account_id: str) -> Result[None]:
        """Get account by id"""

        account_list = self.__account_repo.find_by_id(account_id)

        if account_list:
            return Result.ok(account_list)
