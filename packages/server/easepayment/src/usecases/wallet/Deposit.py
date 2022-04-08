from typing import Type

from ...repositories import IWalletRepository

from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result


class Deposit(IUseCase[None, Result[None]]):
    def __init__(self, wallet_repo: Type[IWalletRepository]) -> None:
        self.__wallet_repo = wallet_repo

    def execute(self, user_id: str, amount: float) -> Result[None]:
        """Initialize the wallet"""

        get_user = self.__wallet_repo.get_by_id(user_id)

        if not get_user:
            return Result.fail("Invalid user")

        sum_balance = get_user[1] + amount

        deposit_in_a_account = self.__wallet_repo.deposit(
            amount=sum_balance, user_id=user_id
        )

        if deposit_in_a_account:
            return Result.ok(f"Deposited {amount} in your account")
