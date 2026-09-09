class College:
    def __init__(self):
        self.name=""
        self.location=""
        self.contact=""
    def college_data(self):
        self.name=input("Enter the college name:")
        self.location=input("Enter the location:")
        self.contact=int(input("Enter the contact number:"))
    def college_info(self):
        print("..............College details:..............")
        print("College name:",self.name)
        print("Location:",self.location)
        print("Contact_number:",self.contact)
class Department(College):
    def __init__(self):
        self.id=""
        self.name=""
        self.HOD=""
    def dept_data(self):
        self.id=int(input("Enter the Department id:"))
        self.name=input("Enter the Department name:")
        self.HOD=input("Enter the HOD name:")
    def dept_info(self):
        print(".................Department details:..............")
        print("Department id:",self.id)
        print("Department name:",self.name)
        print("HOD:",self.HOD)
class Student(Department):
    def __init__(self):
        self.id=""
        self.name=""
        self.course=""
        self.place=""
        self.mobile=""
    def student_data(self):
        self.id =int(input("Enter the student id:"))
        self.name=input("Enter the student name:")
        self.course=input("Enter the course name:")
        self.place=input("Enter the place:")
        self.mobile=int(input("Enter the mobile number:"))
    def student_info(self):
        print(".......Student details:.........")
        print("Student id:", self.id)
        print("Student name:",self.name)
        print("Course:",self.course)
        print("Place:",self.place)
        print("Mobile_number:",self.mobile)
object1=Student()
object1.student_data()
object1.dept_data()
object1.college_data()
object1.student_info()
object1.dept_info()
object1.college_info()