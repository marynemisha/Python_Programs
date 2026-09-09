class Company:                                      #parent class
    def __init__(self):
        self.company_name="Luminar"                  #public variable
    def display_company_info(self):                  #public member function
        #accessing inside the class
        print("Company name:",self.company_name)
class Employee(Company):                             #child class
    def display_employee_info(self):
        #accessing inside the child class
        print("Company name:",self.company_name)

object1=Company()
object1.display_company_info()                       #parent class object

object2=Employee()
object2.display_employee_info()                      #child class object

print(object1.company_name)                          #accessing outside the class

