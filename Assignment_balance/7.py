#Write a Python program to create a calculator class. Include methods for basic
# arithmetic operations.
class Calculator:
    def __init__(self):
        self.n1=int(input("Enter your first number:"))
        self.n2=int(input("Enter your second number:"))
    def add(self):
        add=self.n1+self.n2
        print("Addition:",add)
    def sub(self):
        sub=self.n1-self.n2
        print("Subtraction:",sub)
    def mul(self):
        mul=self.n1*self.n2
        print("Multiplication:",mul)
    def div(self):
        div=self.n1/self.n2
        print("Division:",div)

obj=Calculator()
obj.add()
obj.sub()
obj.mul()
obj.div()