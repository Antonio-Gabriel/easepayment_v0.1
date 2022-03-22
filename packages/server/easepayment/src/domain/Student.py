from uuid import uuid4

from dataclasses import dataclass
from .validators import Email, Phone
from .entityprops import StudentProps

from packages.server._shared.src.core.domain import Entity
from packages.server._shared.src.core.logic import Result, Guard


@dataclass
class StudentPropsResult(StudentProps):
    id: str = None


class Student:
    class __private(Entity[StudentProps]):
        def __init__(self, props: StudentProps, id: int = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: StudentProps, id: int = None):
        """create student object"""

        if not id:
            id = uuid4()

        guard_result = Guard.against_null_or_empty_bulk(
            **{
                "name": props.name,
                "email": props.email,
                "phone": props.phone,
                "process": props.process,
            }
        )

        if props.process < 0 or props.process == 0:
            return Result.fail("Invalid process number")

        if guard_result is not None and not guard_result.succeeded:
            return Result.fail(guard_result.message)

        if not Email.is_valid(props.email):
            return Result.fail("Invalid email address, pleace check your email!")

        if not Phone.is_valid(props.phone):
            return Result.fail("Invalid phone number, pleace check your phone number!")

        student = cls.__private(props, id)

        return Result.ok(
            StudentPropsResult(
                id=id,
                name=student.props.name,
                email=student.props.email,
                phone=student.props.phone,
                avatar=student.props.avatar,
                process=student.props.process,
                district=student.props.district,
                location=student.props.location,
                studentId=student.props.studentId,
            )
        )
