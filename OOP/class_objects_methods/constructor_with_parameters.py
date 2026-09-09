class Student:                                #class
    def __init__(self,name,course):           #constructor method
        self.Student_name=name
        self.Course=course
    def display(self):
        print("_____Student details____")
        print("Name   :",self.Student_name)
        print("Course :",self.Course)
object1=Student("Pranav","Python")
object1.display()

object2=Student("Sree","Java")
object2.display()