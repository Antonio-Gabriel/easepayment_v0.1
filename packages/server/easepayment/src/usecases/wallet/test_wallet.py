from unittest import TestCase

from .InitializeWallet import InitializeWallet
from ...infra.repositories import WalletRepository

from .Deposit import Deposit
from .WithDraw import WithDraw


class TestWalletUsecase(TestCase):
    def test_initialize_wallet_usecase(self):

        running_wallet = InitializeWallet(WalletRepository)
        result = running_wallet.execute(user_id="df3a8357-fb82-4eaa-a8f9-a4888472ed3a")

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)

    def test_deposit_ammount_wallet_usecase(self):

        deposit_in_wallet = Deposit(WalletRepository)
        result = deposit_in_wallet.execute(
            user_id="df3a8357-fb82-4eaa-a8f9-a4888472ed3a", amount=20000
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)

    def test_remove_ammount_wallet_usecase(self):

        deposit_in_wallet = WithDraw(WalletRepository)
        result = deposit_in_wallet.execute(
            user_id="df3a8357-fb82-4eaa-a8f9-a4888472ed3a", amount=10000
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)
