"""
Programs: person_class.py and student_obj.py
Author: Jessie Horvath
Modified: 04/04/2022

The purpose of these programs is to create a child class that inherits
the attributes and methods from a parent class and overrides one of
those methods.
"""
from person_class import Student as s

# Driver
my_student = s(900111111, 'Song', 'River')
print(my_student.display())
my_student = s(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = s(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student