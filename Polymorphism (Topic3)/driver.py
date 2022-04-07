"""
Programs: base_class.py, derived_classes.py, driver.py
Author: Jessie Horvath
Date Modified: 4/6/2022

The purpose of these programs is to write two classes that inherit from a
base class and override their display methods, while adding specific
attributes and methods that are unique to the subclasses.
"""

from dervied_classes import SalariedEmployee as sal
from dervied_classes import HourlyEmployee as hour

salaried_employee = sal("Horvath", "Jessie", "123 Cherry Ln", "555-555-1234", "4/6/2022", 40000)
print(salaried_employee.display())
salaried_employee.give_raise(45000)
print(salaried_employee.display())

hourly_employee = hour("Horvath", "Jessie", "123 Berry Ln", "555-555-4321", "4/6/22", 10.00)
print(hourly_employee.display())
hourly_employee.give_raise(12)
print(hourly_employee.display())