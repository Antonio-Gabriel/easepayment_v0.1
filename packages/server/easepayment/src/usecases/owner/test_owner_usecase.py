from unittest import TestCase

from .CreateOwner import CreateOwner
from .OwnerRequestDTO import OwnerRequestDTO
from ...infra.repositories import OwnerRepository


class TestOwnerUsecase(TestCase):
    def test_owner_usecase_integration(self):

        create_owner = CreateOwner(OwnerRepository)
        result = create_owner.execute(
            OwnerRequestDTO(
                name="António Gabriel",
                email="antoniogabriel@gmail.com",
                phone="+244923565442",
            )
        )

        error = result.error_value()

        if error:
            print(result.error_value())

        print(result.get_value().id)

        self.assertTrue(True)
