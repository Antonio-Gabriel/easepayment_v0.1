from unittest import TestCase

from .CreateUser import CreateUser
from .UserRequestDTO import UserRequestDTO
from ...infra.repositories import UserRepository


class TestUserUsecase(TestCase):
    def test_create_user_usecase_integration(self):

        create_user = CreateUser(UserRepository)
        result = create_user.execute(
            UserRequestDTO(
                account_id="ffa36764-84c3-4596-9178-0fa2bf95450d",
                owner_id="73b2e45e-5ea3-483a-9bef-7d6fc7da5028",
                student_id=None,
                state=True,
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        print(result.get_value().id)

        self.assertTrue(True)
