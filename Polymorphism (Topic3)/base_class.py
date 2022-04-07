class Employee:
    # Constructor
    def __init__(self, lname, fname, address, phone_number):
        self.last_name = lname
        self.first_name = fname
        self._address = address
        self.phone = phone_number

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname
    
    def set_address(self, address):
        self._address = address
    
    def set_phone(self, phone):
        self.phone_number = phone


    def display(self):
        return str(self.first_name) + " " + str(self.last_name) + "\n" + str(self._address) + "\n" + str(self.phone)