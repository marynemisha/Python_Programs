class Employee:
    def company(self):
        print("company name is:  Luminar Technolab....")
class Manager(Employee):
    def manage(self):
        print("Manager manages the team.....")
class Developer(Employee):
    def code(self):
        print("Developer writes code.....")
obj1=Manager()
obj1.company()
obj1.manage()

obj2=Developer()
obj2.company()
obj2.code()