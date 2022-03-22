from typing import Type

from ....repositories import IStudentAutoRelated


class StudentAutoRelatedEvent:
    def __init__(self, related_repo: Type[IStudentAutoRelated]):
        self.__related_repo = related_repo

    def dispatch(self, owner_student_id: str, student_id: str):
        result = self.__related_repo.save(owner_student_id, student_id)

        if result:
            return result
