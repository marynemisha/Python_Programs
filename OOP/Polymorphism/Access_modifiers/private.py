class Employee:
    def __init__(self):
        self.name="Anu"                    #public
        self.__salary=20000                #private
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.__salary)

obj=Employee()
obj.display()

print("Outside the class:")
print(obj.name)           #public
print(obj.__salary)       #private
