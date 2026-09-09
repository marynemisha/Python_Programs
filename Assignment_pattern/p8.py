#Hollow Inverted Right-Angled Triangle Pattern
rows=int(input("Enter a number :"))
for i in range(rows):
    for j in range(rows-i):
        if i == 0 or j == 0 or j == rows-i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()