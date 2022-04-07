from tracemalloc import start
from base_class import Employee
class SalariedEmployee(Employee):
    def __init__(self, lname, fname, address, phone_number, start_date, salary):
        super().__init__(lname, fname, address, phone_number)
        self.start_date = start_date
        self.salary = salary

    def set_start_date(self, date):
        self.start_date = date

    def set_salary(self, salary):
        self.salary = salary
    
    def give_raise(self, new_sal):
        self.salary = new_sal
    
    def display(self):
        return "Employee: " + self.first_name + " " + self.last_name + "\nAddress: " + self._address + "\nPhone Number: " + self.phone + "\nStart Date: " + self.start_date + "\nSalary: $" + str(self.salary)


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, address, phone_number, start_date, hourly_pay):
        super().__init__(lname, fname, address, phone_number)
        self.start_date = start_date
        self.hourly_pay = hourly_pay
    
    def set_start_date(self, date):
        self.start_date = date
    
    def set_hourly_pay(self, pay):
        self.hourly_pay = pay

    def give_raise(self, new_pay):
        self.hourly_pay = new_pay
    
    def display(self):
        return "Employee: " + self.first_name + " " + self.last_name + "\nAddress: " + self._address + "\nPhone Number: " + self.phone + "\nStart Date: " + self.start_date + "\nHourly Pay: $" + str(f"{self.hourly_pay:.2f}")
