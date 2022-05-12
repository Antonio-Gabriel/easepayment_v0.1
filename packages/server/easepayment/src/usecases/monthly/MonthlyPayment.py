from typing import Type
from uuid import uuid4
from datetime import datetime

from packages.server.easepayment.src.infra.repositories.PaymentRepository import (
    PaymentRepository,
)
from ...domain import Payment
from packages.server._shared import IUseCase
from ...repositories import IMonthlyRepository
from .MonthlyRequestDTO import MonthlyRequestDTO
from .MonthAlreadyPayed import MonthAlreadyPayed
from packages.server._shared.src.core.logic import Result


class MonthlyPayment(IUseCase[MonthlyRequestDTO, Result[None]]):
    def __init__(self, monthly_repo: Type[IMonthlyRepository]) -> None:
        self.__monthly_repo = monthly_repo

    def execute(self, request: MonthlyRequestDTO) -> Result[None]:
        """Monthly Payed"""

        month_already_payed = self.__monthly_repo.find_montly_payed(
            user_id=request.userId, month=request.month
        )

        if month_already_payed:
            return MonthAlreadyPayed(request.month)

        if datetime.today().day >= 15:
            request.value += 1000

        payment = Payment.create(
            MonthlyRequestDTO(
                userId=request.userId,
                studentId=request.studentId,
                value=request.value,
                month=request.month,
            )
        )

        payment_repo = PaymentRepository
        payment_id = payment_repo.pay(
            payment.get_value().userId,
            payment.get_value().studentId,
            payment.get_value().value,
            str(uuid4()),
        )

        if payment_id:

            response = self.__monthly_repo.pay_month(
                str(uuid4()), payment_id, request.month
            )

            if response:

                return Result.ok("Payed month")
