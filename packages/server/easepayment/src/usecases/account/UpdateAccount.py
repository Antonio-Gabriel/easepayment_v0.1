from typing import Type
from ...domain import Account

from .GetAccountById import GetAccountById

from packages.server._shared import IUseCase
from ...repositories import IAccountRepository

from ...domain.entityprops import AccountProps

from packages.server._shared.src.core.logic import Result
from .UpdateAccountRequestDTO import UpdateAccountRequestDTO


class UpdateAccount(IUseCase[UpdateAccountRequestDTO, Result[None]]):
    def __init__(self, account_repo: Type[IAccountRepository]) -> None:
        self.__account_repo = account_repo

    def execute(self, request: UpdateAccountRequestDTO, id: str) -> Result[None]:
        """Update account"""

        account_result = Account.create(
            UpdateAccountRequestDTO(
                username=request.username,
                password=request.password,
                currentPassword=request.currentPassword,
            )
        )

        if account_result.error_value():
            return Result.fail(account_result.error_value())

        get_account = GetAccountById(self.__account_repo)
        result = get_account.execute(account_id=id)

        if not request.currentPassword and not request.password:

            account_update_result = self.__account_repo.update(
                AccountProps(username=request.username, password=result.get_value()[2]),
                id=id,
            )

            if account_update_result:
                return Result.ok(account_result.get_value())

        if Account.compare(request.currentPassword, result.get_value()[2].encode()):
            account_update_result = self.__account_repo.update(
                AccountProps(
                    username=request.username,
                    password=account_result.get_value().password,
                ),
                id=id,
            )

            if account_update_result:
                return Result.ok(account_result.get_value())

        else:
            return Result.fail("Password is not equal")
