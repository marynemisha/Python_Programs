#Write a program to find the missing number from a list containing numbers from 1 to N
list1 = [1, 2, 4, 5]
print(list1)
print("Number of elements:",len(list1))
N = len(list1) + 1
for i in range(1, N+1):
    if i not in list1:
        print("Missing number:", i)