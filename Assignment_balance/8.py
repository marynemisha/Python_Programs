#Write a Python function to find the maximum of three numbers.
def largest(x,y,z):
    largest=max(x,y,z)
    print("Maximum  :",largest)
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))

largest(x,y,z)