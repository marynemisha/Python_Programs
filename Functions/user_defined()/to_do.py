def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
choice=input("Enter your choice:")

if choice=='A' or choice=='a':
    print("sum=",add(a,b))
elif choice=='B'or choice=='b':
    print("difference=",sub(a,b))
elif choice=='C'or choice=='c':
    print("multiplication=",mul(a, b))
elif choice=='D' or choice=='d':
    print("division=",div(a,b))
else:
    print("Invalid")