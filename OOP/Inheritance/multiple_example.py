class Person:
    def __init__(self):
        self.name=""
        self.age=""
        self.place=""
        self.mobile=""
        self.email=""
    def person_data(self):
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        self.place=input("Enter the place:")
        self.mobile=int(input("Enter the mobile number:"))
        self.email=input("Enter the email id:")
    def person_info(self):
        print("..............Person details................")
        print("Name         :",self.name)
        print("Age          :",self.age)
        print("Place        :",self.place)
        print("Mobile Number:",self.mobile)
        print("Email id     :",self.email)
class Salary:
    def __init__(self):
        self.basic_salary=""
        self.bonus=""
        self.doj=""
    def salary_data(self):
        self.basic_salary=int(input("Enter the basic salary:"))
        self.bonus=int(input("Enter the bonus:"))
        self.doj=int(input("Enter the date of joining:"))
    def salary_info(self):
        print("..............Salary details.............")
        print("Basic salary     :",self.basic_salary)
        print("Bonus            :",self.bonus)
        print("Date of joining  :",self.doj)
class Employee:
    def __init__(self):
        self.emp_id=""
        self.designation=""
    def employee_data(self):
        self.emp_id=int(input("Enter the employee id:"))
        self.designation=input("Enter the designation:")
    def employee_info(self):
        print("................Employee details...............")
        print("Employee id    :",self.emp_id)
        print("Designation    :",self.designation)

obj=Employee()
obj1=Person()
obj2=Salary()
obj1.person_data()
obj2.salary_data()
obj.employee_data()
obj1.person_info()
obj2.salary_info()
obj.employee_info()