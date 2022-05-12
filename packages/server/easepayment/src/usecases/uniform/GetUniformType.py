from typing import Type
from packages.server._shared import IUseCase
from ...repositories import IUniformRepository
from packages.server._shared.src.core.logic import Result


class GetUniformType(IUseCase[None, Result[None]]):
    def __init__(self, uniform_repo: Type[IUniformRepository]) -> None:
        self.__uniform_repo = uniform_repo

    def execute(self) -> Result[None]:
        """Get uniform type"""

        get_uniform_types = self.__uniform_repo.get_uniform_type()

        if get_uniform_types:
            return Result.ok(get_uniform_types)
