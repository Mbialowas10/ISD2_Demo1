from student.istudent import IStudent

class StudentDecorator(IStudent):
    def __init__(self, student:IStudent):
        self.__student = student
    
    @property
    def grade_point_average(self) -> float:
        return self.__student.grade_point_average

