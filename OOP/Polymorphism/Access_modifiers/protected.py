class Student:                    #parent class
    def __init__(self):
        self._marks=92            #protected variable
    def display(self):
        #accessing in the same class
        print("Marks  :",self._marks)
class Myclass(Student):
    def student_data(self):
        #accessing in the child class
        print("............Student details.............")
        print("Total marks:",self._marks)

obj=Myclass()  #child class calling
obj.display()
obj.student_data()
#accessing is possible outside the class
print(obj._marks)