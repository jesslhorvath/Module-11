"""
Programs: manager.py, parent_classes.py, driver.py
Author: Jessie Horvath
Date Modified: 4/6/2022

The purpose of these programs is to create a class that inherits from multiple
parents. This class accepts a list of objects (employees) and returns them in 
its display() function.
"""

from manager import Manager as m
from parent_classes import Employee as e

emp1 = e("Bob", "Ross", "2/1/2022", 30000)
emp2 = e("Janet", "Jackson", "3/4/1986", 95000)
emp3 = e("Fred", "Flintstone", "5/26/2011", 76000)

emp_list = [emp1, emp2, emp3]

new_manager = m("Jessie", "Horvath", "4/3/2019", 40000, "Sales", emp_list)
print(new_manager.display())

new_manager.give_raise(42000)
print(new_manager.display())