from typing import Type
from uuid import uuid4
from packages.server._shared import IUseCase
from ...repositories import IUniformRepository
from .UniformTypeRequestDTO import UniformTypeRequestDTO
from packages.server._shared.src.core.logic import Result


class CreateUniformType(IUseCase[UniformTypeRequestDTO, Result[None]]):
    def __init__(self, uniform_repo: Type[IUniformRepository]) -> None:
        self.__uniform_repo = uniform_repo

    def execute(self, request: UniformTypeRequestDTO) -> Result[None]:
        """Create uniform type"""

        uniform_type_save_result = self.__uniform_repo.save_uniform_type(
            str(uuid4()), request.type, request.price
        )

        if uniform_type_save_result:
            return Result.ok("Created uniform type")
