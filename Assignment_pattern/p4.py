#Inverted Right-Angled Triangle in Python
rows=int(input("Enter a number:"))
for i in range(rows,0,-1):
    for s in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()