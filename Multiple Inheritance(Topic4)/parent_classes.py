class Person:
    def __init__(self, lname, fname, add, phone):
        self.last_name = lname
        self.first_name = fname
        self.address = add
        self.phone_num = phone

    def display(self):
        return "Name : " + str(self.first_name) + " " + str(self.last_name) + "\nAddress: " + str(self.address) + "\nPhone: " + str(self.phone_num)


class Employee:
    def __init__(self, fname, lname, start_date, salary):
        self.first_name = fname
        self.last_name = lname
        self.start_date = start_date
        self.salary = salary
    
    def give_raise(self, new_sal):
        self.salary = new_sal

    def __repr__(self):
        return "Employee: " + self.first_name + " " + self.last_name + "\nStart Date: " + self.start_date + "\nSalary: $" + str(self.salary)
    
    def display(self):
        return "Name: " + self.first_name + " \n" + self.last_name + "Start date: " + str(self.start_date) + "\nSalary: " + str(self.salary)
