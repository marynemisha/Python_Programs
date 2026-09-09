#Write a Python program that executes division and handles an ArithmeticError
# exception if there is an arithmetic error.
try:
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    result=n1/n2
    print("Result:", result)
except ArithmeticError:
    print("Arithmetic error....!")
