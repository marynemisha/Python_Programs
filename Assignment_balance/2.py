#Write a Python program to handle a ZeroDivisionError exception when dividing
#a number by zero.
try:
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    result=n1/n2
    print("Result:",result)
except ZeroDivisionError:
    print("Division by zero....!")
