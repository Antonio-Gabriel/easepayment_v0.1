from typing import Type
from ...domain import Account
from packages.server._shared import IUseCase
from .AccountRequestDTO import AccountRequestDTO
from ...repositories import IAccountRepository
from packages.server._shared.src.core.logic import Result


class CreateAccount(IUseCase[AccountRequestDTO, Result[None]]):
    def __init__(self, account_repo: Type[IAccountRepository]) -> None:
        self.__account_repo = account_repo

    def execute(self, request: AccountRequestDTO) -> Result[None]:
        """Create account"""

        account_result = Account.create(
            AccountRequestDTO(username=request.username, password=request.password)
        )

        if account_result.error_value():
            return Result.fail(account_result.error_value())

        account_save_result = self.__account_repo.save(account_result.get_value())

        if account_save_result:
            return Result.ok(account_result.get_value())
