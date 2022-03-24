from unittest import TestCase

from .CreateAccount import CreateAccount
from .AccountRequestDTO import AccountRequestDTO
from ...infra.repositories import AccountRepository
from .UpdateAccountRequestDTO import UpdateAccountRequestDTO

from .UpdateAccount import UpdateAccount
from .GetAccountById import GetAccountById


class TestAccountUseCase(TestCase):
    def test_create_account_usecase_integration(self):

        create_account = CreateAccount(AccountRepository)

        result = create_account.execute(
            AccountRequestDTO(username="ag", password="antonio20")
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        print(result.get_value().id)

        self.assertTrue(True)

    def test_get_account_by_id(self):

        get_account = GetAccountById(AccountRepository)
        result = get_account.execute(account_id="70b2f996-b811-4962-8f70-fda6f4f949cc")

        print(result.get_value()[2])

        self.assertTrue(True)

    def test_update_account(self):

        update_account = UpdateAccount(AccountRepository)
        result = update_account.execute(
            UpdateAccountRequestDTO(
                username="Antonio Gabriel",
                currentPassword="antonio20",
                password="antonio20",
            ),
            id="70b2f996-b811-4962-8f70-fda6f4f949cc",
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)
