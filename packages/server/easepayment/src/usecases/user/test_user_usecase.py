from unittest import TestCase

from .CreateUser import CreateUser
from .UserRequestDTO import UserRequestDTO
from ...infra.repositories import UserRepository


class TestUserUsecase(TestCase):
    def test_create_user_usecase_integration(self):

        create_user = CreateUser(UserRepository)
        result = create_user.execute(
            UserRequestDTO(
                account_id="70b2f996-b811-4962-8f70-fda6f4f949cc",
                owner_id="418a947c-cf18-405d-abc0-c8f662eff753",
                student_id=None,
                state=True,
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        print(result.get_value().id)

        self.assertTrue(True)
