from student.istudent import IStudent

class StudentDecoratoor(IStudent):
    def __init__(self, student:IStudent):
        self.__student = student
    
    @property
    def grade_point_average(self) -> float:
        return self.__grade_point_average

