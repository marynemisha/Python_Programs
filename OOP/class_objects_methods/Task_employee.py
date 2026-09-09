class Employee:
    def __init__(self,id,name,place,company,salary,designation):
        self.id=id
        self.name=name
        self.place=place
        self.company=company
        self.salary=salary
        self.designation=designation
    def display_employee_details(self):
        print("____Employee details____")
        print("ID            :",self.id)
        print("Name          :",self.name)
        print("Place         :",self.place)
        print("Company       :",self.company)
        print("Salary        :",self.salary)
        print("Designation   :",self.designation)

obj1=Employee(101,"Ammu","EKM","TCS",15000,"Developer")
obj1.display_employee_details()
obj2=Employee(102,"Amal","TVM","Wipro",18000,"Engineer")
obj2.display_employee_details()
obj3=Employee(103,"Anju","Calicut","Infosys",50000,"Senior Engineer")
obj3.display_employee_details()   