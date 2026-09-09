#right triangle pattern using nested loop

rows=int(input("Enter a number :"))
#outer loop for handling the rows
for i in range(rows):
    #inner loop for handling the columns
    for j in range(i+1):
        print("*", end=" ")
    print( )