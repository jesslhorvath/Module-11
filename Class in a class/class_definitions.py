"""
Program(s): class_definitions.py and object_definitions.py
Author: Jessie Horvath
Modified: 04/03/2022

The purpose of these programs is to create a class that uses another class's
object and displays a string of the information.
"""
class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):   
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy
    
    def display(self):
        return str(self.first_name) + " " + str(self.last_name) + "\nAddress: " + str(self.address) + "\n"

class Student:
    """Student class"""
    def __init__(self, person, major, start_date, gpa):
        major_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- ")
        if not major_char.issuperset(major):
            raise ValueError
        self.student = person
        self.major = major
        self.start = start_date
        self.gpa = gpa

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display(self):
        return str(self.student.display()) + "Major: " + str(self.major) + ", Start date: " + str(self.start) + ", GPA:" + str(self.gpa)