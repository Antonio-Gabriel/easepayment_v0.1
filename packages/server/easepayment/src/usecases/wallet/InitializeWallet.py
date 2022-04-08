from typing import Type

from ...repositories import IWalletRepository

from ...domain import Wallet
from ...domain.entityprops import WallerProps

from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result


class InitializeWallet(IUseCase[None, Result[None]]):
    def __init__(self, wallet_repo: Type[IWalletRepository]) -> None:
        self.__wallet_repo = wallet_repo

    def execute(self, user_id: str) -> Result[None]:
        """Initialize the wallet"""

        wallet_props = Wallet.create(WallerProps(userId=user_id))

        wallet_initialized = self.__wallet_repo.initialize(wallet_props.get_value())

        if not wallet_initialized:
            return Result.fail("Error for initialize the wallet")

        return Result.ok("Wallet initialized")
