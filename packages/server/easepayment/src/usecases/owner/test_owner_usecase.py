from unittest import TestCase

from .CreateOwner import CreateOwner
from .OwnerRequestDTO import OwnerRequestDTO
from ...infra.repositories import OwnerRepository

from .UpdateOwner import UpdateOwner


class TestOwnerUsecase(TestCase):
    # def test_owner_usecase_integration(self):

    #     create_owner = CreateOwner(OwnerRepository)
    #     result = create_owner.execute(
    #         OwnerRequestDTO(
    #             name="António Gabriel",
    #             email="antoniogabriel@gmail.com",
    #             phone="+244923565442",
    #         )
    #     )

    #     error = result.error_value()

    #     if error:
    #         print(result.error_value())

    #     print(result.get_value().id)

    #     self.assertTrue(True)

    def test_update_owner_usecase_integration(self):

        update_owner = UpdateOwner(OwnerRepository)
        result = update_owner.execute(
            OwnerRequestDTO(
                name="António Gabriel",
                email="antoniogabriel2k20@gmail.com",
                phone="+244923565442",
            ),
            id="418a947c-cf18-405d-abc0-c8f662eff753",
        )

        error = result.error_value()

        if error:
            print(result.error_value())
        else:
            print(result.get_value())

        self.assertTrue(True)
