from typing import Type
from uuid import uuid4
from packages.server._shared import IUseCase
from ...repositories import IUniformRepository
from .UniformPaymentRequestDTO import UniformPaymentRequestDTO
from packages.server._shared.src.core.logic import Result
from packages.server.easepayment.src.infra.repositories import PaymentRepository


class UniformPayment(IUseCase[UniformPaymentRequestDTO, Result[None]]):
    def __init__(self, uniform_repo: Type[IUniformRepository]) -> None:
        self.__uniform_repo = uniform_repo

    def execute(self, request: UniformPaymentRequestDTO) -> Result[None]:
        """Pay uniform"""

        payment_repo = PaymentRepository
        payment_id = payment_repo.pay(
            request.userId,
            request.studentId,
            request.amount,
            str(uuid4()),
        )

        pay_uniform_result = self.__uniform_repo.pay_uniform(
            str(uuid4()), request.uniform_type_type, payment_id
        )

        if pay_uniform_result:
            return Result.ok("Uniform payed")
