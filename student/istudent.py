from abc import ABC, abstractmethod

class IStudent(ABC):
    """Interface for student
    """
    @abstractmethod
    def grade_point_average(self) -> float:
        pass