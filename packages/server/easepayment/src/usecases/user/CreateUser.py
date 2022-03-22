from typing import Type
from ...domain import User
from .UserRequestDTO import UserRequestDTO
from ...repositories import IUserRepository

from packages.server._shared import IUseCase
from packages.server._shared.src.core.logic import Result


class CreateUser(IUseCase[UserRequestDTO, Result[None]]):
    def __init__(self, user_repo: Type[IUserRepository]) -> None:
        self.__user_repo = user_repo

    def execute(self, request: UserRequestDTO) -> Result[None]:

        user_result = User.create(
            UserRequestDTO(
                account_id=request.account_id,
                owner_id=request.owner_id,
                student_id=request.student_id,
                state=True,
            )
        )

        if user_result.error_value():
            return Result.fail(user_result.error_value())

        user_save_result = self.__user_repo.save(user_result.get_value())

        if user_save_result:
            return Result.ok(user_result.get_value())
