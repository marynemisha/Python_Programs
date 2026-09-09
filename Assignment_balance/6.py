# Write a Python program to create a person class. Include attributes like name,
# country and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self):
        self.name=input("Enter your name:")
        self.country=input("Enter your country:")
        self.dob=int(input("Enter your date of birth:"))
    def age(self):
        current=int(input("Enter the current year:"))
        age=current-self.dob
        print("Name        :",self.name)
        print("Country     :",self.country)
        print("DOB         :",self.dob)
        print("Age         :",age)
obj=Person()
obj.age()
