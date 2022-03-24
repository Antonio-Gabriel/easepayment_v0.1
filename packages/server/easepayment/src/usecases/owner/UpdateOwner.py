from typing import Type
from ...domain import Owner
from packages.server._shared import IUseCase
from .OwnerRequestDTO import OwnerRequestDTO
from ...repositories import IOwnerRepository
from .OwnerAlreadyExists import OwnerAlreadyExists
from .PhoneAlreadyExists import PhoneAlreadyExists
from packages.server._shared.src.core.logic import Result


class UpdateOwner(IUseCase[OwnerRequestDTO, Result[None]]):
    def __init__(self, owner_repo: Type[IOwnerRepository]) -> None:
        self.__owner_repo = owner_repo

    def execute(self, request: OwnerRequestDTO, id: str) -> Result[None]:
        """Update owner"""

        owner_result = Owner.create(
            OwnerRequestDTO(
                name=request.name, phone=request.phone, email=request.email
            ),
            id=id,
        )

        if owner_result.error_value():
            return Result.fail(owner_result.error_value())

        get_current_owner = self.__owner_repo.get_by_id(id)

        if (
            get_current_owner[2] != request.phone
            and get_current_owner[3] != request.email
        ):

            owner_already_exists = self.__owner_repo.find_by_email(request.email)
            phone_number_already_exists = self.__owner_repo.find_by_phone(request.phone)

            if owner_already_exists:
                return OwnerAlreadyExists(request.email)

            if phone_number_already_exists:
                return PhoneAlreadyExists(request.phone)

        owner_save_result = self.__owner_repo.update(owner_result.get_value())

        if owner_save_result:

            return Result.ok(owner_result.get_value())
