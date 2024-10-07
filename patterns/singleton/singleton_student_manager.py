class SingletonStudentManager:
    """
    SingletonStudentManager:  Employs singleton pattern to 
    ensure only one instance of the class is in memory at a time.
    """

    """
    Class attributes - defined at the class level in the absence
    of a __init__ method.
    Attributes:
        __instance: Represents the instance of the class in memory.
        __next_student_number:  Keeps track of the next available
            student number.

    """
    __instance = None
    __next_student_number = 20240000

    def __new__(cls):
            """
            Constructs the SingletonStudentManager instance but 
            only if it does not already exist in memory.
            """
            # if there is no instance of this class in memory:
            if not cls.__instance:
                # create the instance
                cls.__instance = super(
                    SingletonStudentManager, cls).__new__(cls)
            
            # return the instance that was in memory
            # or if there wasn't one in memory, return the 
            # instance that was just created.
            return cls.__instance

    def get_next_student_number(self) -> int:
        """
        Returns the next available student number 
        and increments the value for the next use.
        Returns:
            int: next available student number
        """
        student_number = self.__next_student_number
        self.__next_student_number += 1
        return student_number
