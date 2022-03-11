from typing import Type
from ...domain import Student
from packages.server._shared import IUseCase
from .StudentRequestDTO import StudentRequestDTO
from ...repositories import IStudentRepository
from .StudentAlreadyExists import StudentAlreadyExists
from .PhoneAlreadyExists import PhoneAlreadyExists
from .ProcessAlreadyExists import ProcessAlreadyExists

from packages.server._shared.src.core.logic import Result


class CreateStudent(IUseCase[StudentRequestDTO, Result[None]]):
    def __init__(self, student_repo: Type[IStudentRepository]) -> None:
        self.__student_repo = student_repo

    def execute(self, request: StudentRequestDTO) -> Result[None]:
        """Create owner"""

        student_already_exists = self.__student_repo.find_by_email(request.email)
        phone_number_already_exists = self.__student_repo.find_by_phone(request.phone)
        process_already_exists = self.__student_repo.find_by_process(request.process)

        if student_already_exists:
            return StudentAlreadyExists(request.email)

        if phone_number_already_exists:
            return PhoneAlreadyExists(request.phone)

        if process_already_exists:
            return ProcessAlreadyExists(request.process)

        student_result = Student.create(
            StudentRequestDTO(
                name=request.name,
                phone=request.phone,
                email=request.email,
                process=request.process,
                avatar=request.avatar,
                district=request.district,
                location=request.location,
                studentId=request.studentId,
            )
        )

        if student_result.error_value():
            return Result.fail(student_result.error_value())

        student_save_result = self.__student_repo.save(student_result.get_value())

        if student_save_result:

            return Result.ok(student_result.get_value())
