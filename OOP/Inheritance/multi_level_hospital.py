class Hospital:
    def __init__(self):
        self.hp_name=""
        self.location=""
        self.contact=""
    def hp_data(self):
        self.hp_name=input("Enter the hospital name:")
        self.location=input("Enter the location:")
        self.contact=int(input("Enter the contact number:"))
    def hp_info(self):
        print(".........................Hospital Details.............................")
        print("Hospital Name     :",self.hp_name)
        print("Location          :",self.location)
        print("Contact Number    :",self.contact)
class Department(Hospital):
    def __init__(self):
        self.id=""
        self.dept_name=""
        self.HOD_name=""
    def dept_data(self):
        obj.hp_data()
        self.id=int(input("Enter the department id:"))
        self.dept_name=input("Enter the department name:")
        self.HOD_name=input("Enter the HOD name:")
    def dept_info(self):
        obj.hp_info()
        print(".........................Department Details.............................")
        print("Department Id     :", self.id)
        print("Department Name   :", self.dept_name)
        print("HOD Name          :", self.HOD_name)
class Patient(Department):
    def __init__(self):
        self.p_id=""
        self.name=""
        self.age=""
        self.place=""
        self.illness=""
        self.number=""
    def p_data(self):
        obj.dept_data()
        self.p_id=int(input("Enter the patient id:"))
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        self.place=input("Enter the place:")
        self.illness=input("Enter the illness details:")
        self.number=int(input("Enter the contact number:"))
    def p_info(self):
        obj.dept_info()
        print(".........................Patient Details.............................")
        print("Patient Id        :", self.p_id)
        print("Patient Name      :", self.name)
        print("Age               :", self.age)
        print("Place             :", self.place)
        print("Illness Details   :", self.illness)
        print("Contact Number    :", self.number)
obj=Patient()
obj.p_data()
obj.p_info()

