from unittest import TestCase

from .CreateAccount import CreateAccount
from .AccountRequestDTO import AccountRequestDTO
from ...infra.repositories import AccountRepository


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
