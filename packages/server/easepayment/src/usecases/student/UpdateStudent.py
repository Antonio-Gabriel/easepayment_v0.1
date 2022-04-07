from typing import Type
from ...domain import Student
from packages.server._shared import IUseCase

from ...repositories import IStudentRepository
from .StudentRequestDTO import StudentRequestDTO
from .PhoneAlreadyExists import PhoneAlreadyExists
from .StudentAlreadyExists import StudentAlreadyExists

from packages.server._shared.src.core.logic import Result


class UpdateStudent(IUseCase[StudentRequestDTO, Result[None]]):
    def __init__(self, student_repo: Type[IStudentRepository]) -> None:
        self.__student_repo = student_repo

    def execute(self, request: StudentRequestDTO) -> Result[None]:
        """Create owner"""

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

        get_current_student = self.__student_repo.find_by_process(request.process)

        if not get_current_student:
            return Result.fail("Student Not exists")

        if (
            get_current_student[3] != request.phone
            and get_current_student[4] != request.email
        ):

            student_already_exists = self.__student_repo.find_by_email(request.email)
            phone_number_already_exists = self.__student_repo.find_by_phone(
                request.phone
            )

            if student_already_exists:
                return StudentAlreadyExists(request.email)

            if phone_number_already_exists:
                return PhoneAlreadyExists(request.phone)

        student_save_result = self.__student_repo.update(student_result.get_value())

        if student_save_result:

            return Result.ok(student_result.get_value())
