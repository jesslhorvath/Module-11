from tkinter import E
from parent_classes import Employee as e
from parent_classes import Person as p

class Manager(e, p):
    def __init__(self, fname, lname, start_date, salary, department, report_list):
        super().__init__(fname, lname, start_date, salary)
        self.department = department
        self.direct_reports = report_list
    
    def display(self):
        return "Manager: " + self.first_name + " " + self.last_name + "\nStart Date: " + self.start_date + "\nSalary: $" + str(self.salary) + "\nDirect Reports: " + str(self.direct_reports)