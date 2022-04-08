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
    def get():
        """Get All students"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(student_id: str):
        """Get student by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def save(student_props: StudentProps):
        """Save student into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def update(student_props: StudentProps):
        """Update student into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(process: str):
        """Delete student into db"""

        raise NotImplementedError("Method not implemented")
