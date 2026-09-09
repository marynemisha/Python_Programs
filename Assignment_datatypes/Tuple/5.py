#Write a program to find the index of a given element without using the index() method.

tuple1 = (10, 20, 30, 40, 50)
print(tuple1)
print("Number of elements:", len(tuple1))

num = int(input("Enter the element: "))
for i in range(len(tuple1)):
    if tuple1[i] == num:
        print("Index:", i)
        break
