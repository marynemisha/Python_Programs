# Diamond pattern in Python
rows=int(input("Enter a number:"))
#outer loop
for i in range(rows):
    for s in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
#inner loop
for i in range(rows,0,-1):
    for s in range(rows-i+1):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()