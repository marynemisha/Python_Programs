#Hollow Square Pattern in Python
rows=int(input("Enter a number:"))
for i in range(rows):
    for j in range(rows):
        if i==0 or i==rows-1:
            print("*",end=" ")
        elif j==0 or j==rows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()