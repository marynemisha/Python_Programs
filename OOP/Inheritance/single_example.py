class Company:
    def __init__(self):
        self.name=""
        self.location=""
    def company_data(self):
        self.name=input("Enter the company name:")
        self.location=input("Enter the location:")
    def company_info(self):
        print("___Company details___")
        print("Company name:",self.name)
        print("Location  :",self.location)
class Employee(Company):
    def __init__(self):
        self.name=""
        self.email=""
        self.designation=""
        self.place=""
    def employee_data(self):
        self.name=input("Enter the name:")
        self.email=input("Enter the email:")
        self.designation=input("Enter the designation:")
        self.place=input("Enter the place:")
    def employee_info(self):
        print("___Employee details___")
        print("Name:",self.name)
        print("Email:",self.email)
        print("Designation:",self.designation)
        print("Place:",self.place)

obj1=Employee()
obj1.employee_data()
obj1.company_data()
obj1.company_info()
obj1.employee_info()


