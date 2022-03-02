from typing import Type
from ...domain import Owner
from packages.server._shared import IUseCase
from .OwnerRequestDTO import OwnerRequestDTO
from ...repositories import IOwnerRepository
from .OwnerAlreadyExists import OwnerAlreadyExists
from .PhoneAlreadyExists import PhoneAlreadyExists
from packages.server._shared.src.core.logic import Result


class CreateOwner(IUseCase[OwnerRequestDTO, Result[None]]):
    def __init__(self, owner_repo: Type[IOwnerRepository]) -> None:
        self.__owner_repo = owner_repo

    def execute(self, request: OwnerRequestDTO) -> Result[None]:
        """Create owner"""

        owner_already_exists = self.__owner_repo.find_by_email(request.email)
        phone_number_already_exists = self.__owner_repo.find_by_phone(request.phone)

        if owner_already_exists:
            return OwnerAlreadyExists(request.email)

        if phone_number_already_exists:
            return PhoneAlreadyExists(request.phone)

        owner_result = Owner.create(
            OwnerRequestDTO(name=request.name, phone=request.phone, email=request.email)
        )

        if owner_result.error_value():
            return Result.fail(owner_result.error_value())

        owner_save_result = self.__owner_repo.save(owner_result.get_value())

        if owner_save_result:

            return Result.ok(owner_result.get_value())
