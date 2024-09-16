from department.department import Department
from abc import ABC, abstractmethod

class Course(ABC):
    """
     Course Class. Represents a Course taken in a deparment
    """
    def __init__(self, name:str, department:Department, credit_hours:int, capacity:int, current_enrollment:int):
        """
        Initializes a course object based on received arguments (if valid).
        args:
            name (str): The name of the course.
            department (Department): The name of the department in which course is in.
            credit_hours(int): The course credit hours.
            capacity(int):  The number of students that may enroll in the course.
            current_enrollment: The number of students currently enrolled in the course.
        raises:
            ValueError: if any of the arguments are invalid.
        """
        if len(name.strip()) >0:
            self.__name = name
        else:
            raise ValueError("Name cannot be blank")

        if isinstance(department, Department):
            self.__department = department
        else:
            raise ValueError("Department must be one of predefined Departments.")

        if isinstance(credit_hours,int):
            self.__credit_hours = credit_hours
        else:
             raise ValueError("Credit hours must be a whole number.")

        if isinstance(capacity,int):
            # SINGLE underscore for protected attributes
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be numeric")
    @property
    def name(self) -> str:
        """
        Accessor for the name attribute.
        Returns: str - The name associated with the Course instance.
        """
        return self.__name
    
    @property
    def deparment(self) -> Department:
        """
        Accessor for the department attribute.
        Returns: Department - The Department associated with the Course instance.
        """
        return self.__department

    @property
    def credit_hours(self) -> int:
        """
        Accessor for the credit_hours attribute.
        Returns: int - The credit_hours associated with the Course instance.
        """
        return self.__credit_hours
    
    def __str__(self) ->str:
        """
        Returns a string representation of the Course instance.
        Returns: str - The Course instance as a formatted string.
        """
        return (f"Course: {self.__name}"
                + f"\nDepartment: {self.__department.name.replace('_',' ').title()}"
                 + f"\nCredit Hours: {self.__credit_hours}")


        

