from typing import Type
from packages.server.easepayment.src.infra.repositories import AccountRepository
from packages.server.easepayment.src.infra.repositories.UserRepository import (
    UserRepository,
)

from packages.server.easepayment.src.usecases.user.GetUserById import GetUserById
from packages.server.easepayment.src.usecases.user.GetUserByOwnerId import (
    GetUserByOwnerId,
)
from ...repositories import IOwnerRepository

from ...domain import Account

from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result


class SignInUser(IUseCase[None, Result[None]]):
    def __init__(self, user_repo: Type[IOwnerRepository]) -> None:
        self.__user_repo = user_repo

    def execute(self, email: str, password: str) -> Result[None]:
        """Sign in use"""
        email_already_exists = self.__user_repo.find_by_email(email)

        if not email_already_exists:
            return Result.fail("Invalid user or password")

        get_user_id = GetUserByOwnerId(UserRepository)
        result = get_user_id.execute(email_already_exists[0])

        if Account.compare(password, result.get_value()[1].encode()):

            get_user = GetUserById(UserRepository)
            user_result = get_user.execute(result.get_value()[0])

            return Result.ok(user_result.get_value())

        return Result.fail("Invalid user or password!")
