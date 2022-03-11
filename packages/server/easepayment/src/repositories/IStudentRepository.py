from abc import ABC, abstractmethod
from ..domain.entityprops import StudentProps


class IStudentRepository(ABC):
    @abstractmethod
    def find_by_email(email: str):
        """Find student by email"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_by_phone(phone: str):
        """Find student by phone number"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def find_by_process(process: str):
        """Find student by phone number"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def save(student_props: StudentProps):
        """Save student into db"""

        raise NotImplementedError("Method not implemented")
