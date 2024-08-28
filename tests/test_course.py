"""
Description: Unit tests for the Course class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_course.py
"""
import unittest

from course.course import Course
from department.department import Department
class TestClient(unittest.TestCase):
    
    

    def test_init_valid(self):
        course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE,6)

    # Assert (uses name mangling to obtain private attribute)
        self.assertEqual("Intermediate Software Development", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(6, course._Course__credit_hours)


    def test_init_invalid_name_raises_exception(self):
        with self.assertRaises(ValueError):
            course = Course(" ", Department.COMPUTER_SCIENCE, 6)
    
    def test_init_invalid_department_raises_expection(self):
        with self.assertRaises(ValueError):
            course = Course("Intermediate Software Development", None, 6)

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and 
        # provides initial values for the class attributes.
         self.course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, 6)

    def test_name_accessor(self):
        # Arrange done by setUp above...
        # Act and Assert 
        self.assertEqual("Intermediate Software Development", self.course.name)
