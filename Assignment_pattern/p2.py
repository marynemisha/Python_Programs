#Inverted Right-Angled Triangle in Python
rows=int(input("Enter a number:"))
for i in range(rows):
    for j in range(rows-i):
        print("* ",end=" ")
    print()