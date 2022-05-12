from typing import Type

from packages.server._shared import IUseCase
from ...repositories import IMonthlyRepository
from packages.server._shared.src.core.logic import Result


class GetMonthlyPayed(IUseCase[None, Result[None]]):
    def __init__(self, monthly_repo: Type[IMonthlyRepository]) -> None:
        self.__monthly_repo = monthly_repo

    def execute(self, user_id: str) -> Result[None]:
        """Monthly Payed"""

        get_monthly_payed = self.__monthly_repo.get_monthly_payed(user_id)

        return Result.ok(get_monthly_payed)
