from course.course import Course
from department.department import Department

class LectureCourse(Course):
    def __init__(self,name:str,department:Department,
                 credit_hours: int, capacity: int, current_enrollment:int):
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
        super().__init__(name, department,credit_hours)

        if 
