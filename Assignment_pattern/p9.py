rows = int(input("Enter a number: "))

for i in range(rows):
    for s in range(rows-i-1):
        print(" ", end="")

    for j in range(2*i+1):
        if j == 0 or j == 2*i or (i == rows-1 and j % 2 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()