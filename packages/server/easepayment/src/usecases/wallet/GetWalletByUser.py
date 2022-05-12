from typing import Type

from ...repositories import IWalletRepository

from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result


class GetWalletByUser(IUseCase[None, Result[None]]):
    def __init__(self, wallet_repo: Type[IWalletRepository]) -> None:
        self.__wallet_repo = wallet_repo

    def execute(self, user_id: str) -> Result[None]:
        """Get wallet"""

        get_user = self.__wallet_repo.get_user(user_id)

        if get_user:
            return Result.ok(get_user)
