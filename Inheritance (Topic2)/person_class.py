"""
Program(s): person_class.py and student_obj.py
Author: Jessie Horvath
Modified: 04/03/2022

The purpose of these programs is to create a class that inherits
attributes and methods from a parent class and overrides a method from 
the parent class. 
"""
class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):   
        self._last_name = lname
        self._first_name = fname
        self._address = addy


    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address  

class Student(Person):
    def __init__(self, student_id, lname, fname, major="Computer Science", gpa=0.0):
        super().__init__(lname, fname)
        name_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz-'")
        if not (name_char.issuperset(lname) and name_char.issuperset(fname)):
            raise ValueError
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
    
    def display(self):
        return str(self._last_name) + ", " + str(self._first_name) + ":(" + str(self.student_id) + ") " + str(self.major) + " GPA: " + str(self.gpa)
