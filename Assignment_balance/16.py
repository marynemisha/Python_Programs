#Python Program for Sum of squares of first n natural numbers
n=int(input("Enter the number:"))
s=0
for i in range(1,n+1):
    s=s+i*i
print("Sum of squares:",s)