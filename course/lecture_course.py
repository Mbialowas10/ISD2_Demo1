from course.course import Course
from department.department import Department
from student.student import Student

class LectureCourse(Course):
    def __init__(self,name:str,department:Department,
                 credit_hours: int, capacity: int, current_enrollment:int, lecture_hall:str):
        """
        Initializes a LectureCourse object based on received arguments (if valid).
        args:
            name (str): The name of the course.
            department (Department): The name of the department in which course is in.
            credit_hours(int): The course credit hours.
            capacity(int):  The number of students that may enroll in the course.
            current_enrollment: The number of students currently enrolled in the course.
            lecture_hall: The name of the lecture hall in which the course will be delivered. 
        raises:
            ValueError: if any of the arguments are invalid.
        """
        super().__init__(name, department,credit_hours, capacity, current_enrollment)

        if len(lecture_hall.strip()) == 0:
            raise ValueError("Lecrture Hall cannot be blank.")
        else:
            self.__lecture_hall = lecture_hall
    
    def __str__(self) -> str:
        return super().__str__() + f"\nLecture Hall: {self.__lecture_hall}"
    
    def enroll_student(self, student: Student) -> str:
        message = f"{student.name}"
        buffer = int(self._capacity * .10)

        if self._current_enrollment < (self._capacity + buffer):
            self._current_enrollment += 1
            message += f" has been successfully enrolled in the {self.name}."
        else:
            message += f" has NOT been enrolled in the lecture: {self.name} due to insufficient capacity"
        return message

    
