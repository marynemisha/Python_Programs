# Pyramid pattern in Python
rows=int(input("Enter a number:"))
for i in range(rows):
    for s in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
