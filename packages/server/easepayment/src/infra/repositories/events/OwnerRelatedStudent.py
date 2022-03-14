from typing import Type

from ....domain.entityprops import StudentRelatedOwnerProps
from ..OwnerRelatedStudentRepository import OwnerRelatedStudentRepository


class OwnerRelatedStudentEvent:
    def __init__(self, related_repo: Type[OwnerRelatedStudentRepository]):
        self.__related_repo = related_repo

    def dispatch(self, owner_id: str, student_id: str):
        result = self.__related_repo.save(
            StudentRelatedOwnerProps(studentId=student_id, ownerId=owner_id)
        )

        if result:
            return result
